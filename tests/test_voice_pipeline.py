import csv
import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "voice_pipeline.py"
SPEC = importlib.util.spec_from_file_location("voice_pipeline", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class VoicePipelineTests(unittest.TestCase):
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

    def test_extract_uses_embedded_english_not_translation(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "deutsch" / "code" / "scenes").mkdir(parents=True)
            source = root / "deutsch" / "code" / "scenes" / "sample.rpy"
            source.write_text(
                'translate deutsch sample_1234:\n\n'
                '    # arj "Hello there."\n'
                '    arj "Hallo."\n',
                encoding="utf-8",
            )
            docs = root / "docs" / "dutch"
            docs.mkdir(parents=True)
            manifest = docs / "PHASE0_FILE_MANIFEST.csv"
            with manifest.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(
                    handle,
                    fieldnames=["relative_path", "count_reference_language"],
                )
                writer.writeheader()
                writer.writerow(
                    {
                        "relative_path": "code/scenes/sample.rpy",
                        "count_reference_language": "deutsch",
                    }
                )

            old_root = MODULE.ROOT
            try:
                MODULE.ROOT = root
                config = {
                    "source_manifest": "docs/dutch/PHASE0_FILE_MANIFEST.csv",
                    "variables_file": "voice/variables.local.json",
                    "skip_speakers": ["extend"],
                }
                rows, warnings = MODULE.iter_source_rows(config)
            finally:
                MODULE.ROOT = old_root

        self.assertEqual(warnings, [])
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["speaker"], "arj")
        self.assertEqual(rows[0]["english_text"], "Hello there.")
        self.assertEqual(rows[0]["tts_text"], "Hello there.")
        self.assertEqual(rows[0]["status"], "ready")
        self.assertEqual(rows[0]["renpy_id"], "sample_1234")

    def test_extract_marks_variable_line_for_review(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "deutsch").mkdir()
            (root / "deutsch" / "sample.rpy").write_text(
                'translate deutsch sample_5678:\n'
                '    # mc "Hi [mcname]."\n'
                '    mc "Hoi [mcname]."\n',
                encoding="utf-8",
            )
            (root / "manifest.csv").write_text(
                "relative_path,count_reference_language\nsample.rpy,deutsch\n",
                encoding="utf-8",
            )

            old_root = MODULE.ROOT
            try:
                MODULE.ROOT = root
                config = {
                    "source_manifest": "manifest.csv",
                    "variables_file": "voice/variables.local.json",
                    "skip_speakers": ["extend"],
                }
                rows, _ = MODULE.iter_source_rows(config)
            finally:
                MODULE.ROOT = old_root

        self.assertEqual(rows[0]["status"], "needs_review")
        self.assertIn("unresolved-variable:mcname", rows[0]["review_reasons"])


    def test_source_resolver_avoids_conflicting_duplicate_ids(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            for language in ("french", "deutsch"):
                (root / language).mkdir()

            (root / "french" / "sample.rpy").write_text(
                'translate french line_1234:\n'
                '    # mc "Correct line."\n'
                '    mc "Ligne correcte."\n'
                'translate french line_1234:\n'
                '    # mct "Wrong duplicate."\n'
                '    mct "Mauvais doublon."\n',
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
                selected, warnings = MODULE.select_source_file(
                    "sample.rpy",
                    {
                        "count_reference_language": "french",
                        "present_in_languages": "french;deutsch",
                    },
                    {"reference_language_priority": ["deutsch", "french"]},
                )
            finally:
                MODULE.ROOT = old_root

        self.assertIsNotNone(selected)
        self.assertEqual(selected["language"], "deutsch")
        self.assertEqual(len(selected["blocks"]), 1)
        self.assertTrue(any("instead of manifest count reference" in warning for warning in warnings))

    def test_source_resolver_deduplicates_identical_ids(self):
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
                selected, warnings = MODULE.select_source_file(
                    "sample.rpy",
                    {
                        "count_reference_language": "french",
                        "present_in_languages": "french",
                    },
                    {"reference_language_priority": ["french"]},
                )
            finally:
                MODULE.ROOT = old_root

        self.assertEqual(len(selected["blocks"]), 1)
        self.assertEqual(selected["identical_duplicates"], ["line_1234"])
        self.assertTrue(any("deduplicated 1 identical" in warning for warning in warnings))


if __name__ == "__main__":
    unittest.main()
