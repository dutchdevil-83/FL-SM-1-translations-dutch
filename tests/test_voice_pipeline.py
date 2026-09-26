import csv
import json
import importlib.util
import sys
import tempfile
import unittest
from unittest import mock
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "voice_pipeline.py"
SPEC = importlib.util.spec_from_file_location("voice_pipeline", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class VoicePipelineTests(unittest.TestCase):
    def test_merge_character_registry_resets_stale_line_counts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            registry_path = root / "voice" / "characters.json"
            registry_path.parent.mkdir(parents=True)
            registry_path.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "characters": {
                            "jc": {"display_name": "Jerk Cop", "line_count": 38},
                            "mc": {"display_name": "Mike", "line_count": 999},
                        },
                    }
                ),
                encoding="utf-8",
            )

            old_root = MODULE.ROOT
            try:
                MODULE.ROOT = root
                with mock.patch.object(
                    MODULE,
                    "load_manifest",
                    return_value=[
                        {"speaker": "mc"},
                        {"speaker": "mc"},
                    ],
                ):
                    registry = MODULE.merge_character_registry(
                        {"characters_file": "voice/characters.json"},
                        write=False,
                    )
            finally:
                MODULE.ROOT = old_root

        self.assertEqual(registry["characters"]["jc"]["line_count"], 0)
        self.assertEqual(registry["characters"]["mc"]["line_count"], 2)

    def test_prepare_tts_text_removes_formatting_and_preserves_pause(self):
        text, unresolved = MODULE.prepare_tts_text(
            "But it {i}is{/i} true.{w} Really.", {}
        )
        self.assertEqual(text, "But it is true. <short pause> Really.")
        self.assertEqual(unresolved, [])

    def test_prepare_tts_text_marks_unresolved_renpy_variable(self):
        text, unresolved = MODULE.prepare_tts_text(
            "Please tell me, [mcname].", {}
        )
        self.assertEqual(text, "Please tell me, [mcname].")
        self.assertEqual(unresolved, ["mcname"])

    def _write_character_definitions(self, root: Path) -> None:
        path = root / "original-source" / "game" / "code" / "data" / "characters"
        path.mkdir(parents=True, exist_ok=True)
        (path / "names.rpy").write_text(
            'define narrator = Character(None)\n'
            'define mc = Character("[mcname]")\n'
            'define arj = Character("Amber-Rose")\n',
            encoding="utf-8",
        )

    def _write_id_manifest(self, root: Path, relative_path: str, language: str = "deutsch") -> None:
        manifest = root / "manifest.csv"
        with manifest.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(
                handle,
                fieldnames=[
                    "relative_path",
                    "count_reference_language",
                    "present_in_languages",
                ],
            )
            writer.writeheader()
            writer.writerow(
                {
                    "relative_path": relative_path,
                    "count_reference_language": language,
                    "present_in_languages": language,
                }
            )

    def _config(self) -> dict:
        return {
            "original_source_root": "original-source/game",
            "id_manifest": "manifest.csv",
            "id_reference_language_priority": ["deutsch", "french"],
            "variables_file": "voice/variables.local.json",
            "skip_speakers": ["extend"],
        }

    def test_extract_uses_original_source_and_translation_only_for_id(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._write_character_definitions(root)

            direct = root / "original-source" / "game" / "code" / "scenes"
            direct.mkdir(parents=True)
            (direct / "sample.rpy").write_text(
                'label sample:\n'
                '    arj "Hello there."\n',
                encoding="utf-8",
            )

            translated = root / "deutsch" / "code" / "scenes"
            translated.mkdir(parents=True)
            (translated / "sample.rpy").write_text(
                'translate deutsch sample_1234:\n\n'
                '    # arj "Hello there."\n'
                '    arj "Hallo."\n',
                encoding="utf-8",
            )
            self._write_id_manifest(root, "code/scenes/sample.rpy")

            old_root = MODULE.ROOT
            try:
                MODULE.ROOT = root
                rows, warnings = MODULE.iter_source_rows(self._config())
            finally:
                MODULE.ROOT = old_root

        self.assertEqual(warnings, [])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["speaker"], "arj")
        self.assertEqual(rows[0]["english_text"], "Hello there.")
        self.assertEqual(rows[0]["tts_text"], "Hello there.")
        self.assertEqual(rows[0]["status"], "ready")
        self.assertEqual(rows[0]["renpy_id"], "sample_1234")
        self.assertTrue(rows[0]["source_file"].startswith("original-source/game/"))
        self.assertTrue(rows[0]["reference_file"].startswith("deutsch/"))

    def test_extract_marks_variable_line_for_review(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._write_character_definitions(root)

            direct = root / "original-source" / "game"
            (direct / "sample.rpy").write_text(
                'mc "Hi [mcname]."\n',
                encoding="utf-8",
            )
            (root / "deutsch").mkdir()
            (root / "deutsch" / "sample.rpy").write_text(
                'translate deutsch sample_5678:\n'
                '    # mc "Hi [mcname]."\n'
                '    mc "Hoi [mcname]."\n',
                encoding="utf-8",
            )
            self._write_id_manifest(root, "sample.rpy")

            old_root = MODULE.ROOT
            try:
                MODULE.ROOT = root
                rows, _ = MODULE.iter_source_rows(self._config())
            finally:
                MODULE.ROOT = old_root

        self.assertEqual(rows[0]["status"], "needs_review")
        self.assertIn("unresolved-variable:mcname", rows[0]["review_reasons"])

    def test_literal_speaker_is_not_spoken_as_part_of_dialogue(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._write_character_definitions(root)

            direct = root / "original-source" / "game"
            (direct / "sample.rpy").write_text(
                '"BDSM Model" "Hello there."\n',
                encoding="utf-8",
            )
            (root / "deutsch").mkdir()
            (root / "deutsch" / "sample.rpy").write_text(
                'translate deutsch sample_literal:\n'
                '    # "BDSM Model" "Hello there."\n'
                '    "BDSM-Modell" "Hallo."\n',
                encoding="utf-8",
            )
            self._write_id_manifest(root, "sample.rpy")

            old_root = MODULE.ROOT
            try:
                MODULE.ROOT = root
                rows, _ = MODULE.iter_source_rows(self._config())
            finally:
                MODULE.ROOT = old_root

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["speaker"], "")
        self.assertEqual(rows[0]["speaker_label"], "BDSM Model")
        self.assertEqual(rows[0]["english_text"], "Hello there.")
        self.assertEqual(rows[0]["tts_text"], "Hello there.")
        self.assertIn("literal-speaker:BDSM Model", rows[0]["review_reasons"])

    def test_stale_translation_comment_never_replaces_original_source(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._write_character_definitions(root)

            direct = root / "original-source" / "game"
            (direct / "sample.rpy").write_text(
                'arj "Canonical original line."\n',
                encoding="utf-8",
            )
            (root / "deutsch").mkdir()
            (root / "deutsch" / "sample.rpy").write_text(
                'translate deutsch stale_1234:\n'
                '    # arj "Stale metadata line."\n'
                '    arj "Veraltet."\n',
                encoding="utf-8",
            )
            self._write_id_manifest(root, "sample.rpy")

            old_root = MODULE.ROOT
            try:
                MODULE.ROOT = root
                rows, warnings = MODULE.iter_source_rows(self._config())
            finally:
                MODULE.ROOT = old_root

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["english_text"], "Canonical original line.")
        self.assertEqual(rows[0]["renpy_id"], "")
        self.assertIn("renpy-id-not-resolved", rows[0]["review_reasons"])
        self.assertTrue(any("does not match the canonical original source" in warning for warning in warnings))

    def test_narrator_is_resolved_from_original_source(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            self._write_character_definitions(root)

            direct = root / "original-source" / "game"
            (direct / "sample.rpy").write_text('"A quiet room."\n', encoding="utf-8")
            (root / "deutsch").mkdir()
            (root / "deutsch" / "sample.rpy").write_text(
                'translate deutsch narrator_1234:\n'
                '    # "A quiet room."\n'
                '    "Ein ruhiger Raum."\n',
                encoding="utf-8",
            )
            self._write_id_manifest(root, "sample.rpy")

            old_root = MODULE.ROOT
            try:
                MODULE.ROOT = root
                rows, _ = MODULE.iter_source_rows(self._config())
            finally:
                MODULE.ROOT = old_root

        self.assertEqual(rows[0]["speaker"], "narrator")
        self.assertEqual(rows[0]["status"], "ready")
        self.assertEqual(rows[0]["renpy_id"], "narrator_1234")

    def test_id_resolver_avoids_conflicting_duplicate_ids(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for language in ("french", "deutsch"):
                (root / language).mkdir()

            (root / "french" / "sample.rpy").write_text(
                'translate french line_1234:\n'
                '    # mc "Correct line."\n'
                '    mc "Ligne correcte."\n'
                'translate french line_1234:\n'
                '    # arj "Wrong duplicate."\n'
                '    arj "Mauvais doublon."\n',
                encoding="utf-8",
            )
            (root / "deutsch" / "sample.rpy").write_text(
                'translate deutsch line_1234:\n'
                '    # mc "Correct line."\n'
                '    mc "Korrekte Zeile."\n',
                encoding="utf-8",
            )

            old_root = MODULE.ROOT
            try:
                MODULE.ROOT = root
                selected, warnings = MODULE.select_id_metadata_file(
                    "sample.rpy",
                    {
                        "count_reference_language": "french",
                        "present_in_languages": "french;deutsch",
                    },
                    {"id_reference_language_priority": ["deutsch", "french"]},
                )
            finally:
                MODULE.ROOT = old_root

        self.assertIsNotNone(selected)
        self.assertEqual(selected["language"], "deutsch")
        self.assertEqual(len(selected["blocks"]), 1)
        self.assertTrue(any("instead of manifest count reference" in warning for warning in warnings))


    def test_create_genai_client_explicitly_uses_gemini_api_key(self):
        class FakeGenai:
            def __init__(self):
                self.received_api_key = None

            def Client(self, *, api_key):
                self.received_api_key = api_key
                return object()

        fake = FakeGenai()
        with mock.patch.dict(
            MODULE.os.environ,
            {"GEMINI_API_KEY": "gemini-key", "GOOGLE_API_KEY": "stale-google-key"},
            clear=True,
        ):
            with mock.patch.object(MODULE, "require_genai", return_value=fake):
                MODULE.create_genai_client()

        self.assertEqual(fake.received_api_key, "gemini-key")

    def test_gemini_api_key_rejects_empty_value(self):
        with mock.patch.dict(MODULE.os.environ, {}, clear=True):
            with self.assertRaises(SystemExit):
                MODULE.gemini_api_key()

    def test_load_casting_request_accepts_matching_export(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            request_dir = root / "voice" / "build" / "casting" / "requests"
            request_dir.mkdir(parents=True)
            request = {
                "store": True,
                "voice": {
                    "model": "gemini-3.8-flash-tts",
                    "type": "prompted",
                    "display_name": "Mike",
                    "gender": "male",
                    "language_code": "en-US",
                    "prompted": {"input": "Warm adult male voice."},
                },
            }
            (request_dir / "mc.json").write_text(
                json.dumps(request), encoding="utf-8"
            )
            old_root = MODULE.ROOT
            try:
                MODULE.ROOT = root
                path, loaded = MODULE.load_casting_request(
                    {"casting_request_dir": "voice/build/casting/requests", "spoken_language": "en-US"},
                    "mc",
                    {
                        "display_name": "Mike",
                        "language_code": "en-US",
                        "gender": "male",
                        "design_prompt": "Warm adult male voice.",
                    },
                )
            finally:
                MODULE.ROOT = old_root

        self.assertEqual(path.name, "mc.json")
        self.assertEqual(loaded, request)

    def test_load_casting_request_rejects_stale_prompt(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            request_dir = root / "voice" / "build" / "casting" / "requests"
            request_dir.mkdir(parents=True)
            (request_dir / "mc.json").write_text(
                json.dumps({
                    "store": True,
                    "voice": {
                        "model": "gemini-3.8-flash-tts",
                        "type": "prompted",
                        "display_name": "Mike",
                        "gender": "male",
                        "language_code": "en-US",
                        "prompted": {"input": "Old prompt."},
                    },
                }),
                encoding="utf-8",
            )
            old_root = MODULE.ROOT
            try:
                MODULE.ROOT = root
                with self.assertRaises(SystemExit) as context:
                    MODULE.load_casting_request(
                        {"casting_request_dir": "voice/build/casting/requests", "spoken_language": "en-US"},
                        "mc",
                        {
                            "display_name": "Mike",
                            "language_code": "en-US",
                            "gender": "male",
                            "design_prompt": "New prompt.",
                        },
                    )
            finally:
                MODULE.ROOT = old_root

        self.assertIn("stale", str(context.exception))

    def test_id_resolver_deduplicates_identical_ids(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "french").mkdir()
            (root / "french" / "sample.rpy").write_text(
                'translate french line_1234:\n'
                '    # mc "Same line."\n'
                '    mc "Même ligne."\n'
                'translate french line_1234:\n'
                '    # mc "Same line."\n'
                '    mc "Même ligne."\n',
                encoding="utf-8",
            )

            old_root = MODULE.ROOT
            try:
                MODULE.ROOT = root
                selected, warnings = MODULE.select_id_metadata_file(
                    "sample.rpy",
                    {
                        "count_reference_language": "french",
                        "present_in_languages": "french",
                    },
                    {"id_reference_language_priority": ["french"]},
                )
            finally:
                MODULE.ROOT = old_root

        self.assertEqual(len(selected["blocks"]), 1)
        self.assertEqual(selected["identical_duplicates"], ["line_1234"])
        self.assertTrue(any("deduplicated 1 identical" in warning for warning in warnings))


if __name__ == "__main__":
    unittest.main()
