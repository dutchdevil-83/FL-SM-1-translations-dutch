import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "voice_studio.py"
SPEC = importlib.util.spec_from_file_location("voice_studio", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class VoiceStudioTests(unittest.TestCase):
    def test_rate_limiter_spacing_for_three_rpm(self):
        wait = MODULE.PersistentRateLimiter.compute_wait(
            [90.0],
            now=100.0,
            rpm=3,
            safety_margin_seconds=1.5,
        )
        self.assertAlmostEqual(wait, 11.5)

    def test_rate_limiter_rolling_window(self):
        wait = MODULE.PersistentRateLimiter.compute_wait(
            [50.0, 70.0, 90.0],
            now=100.0,
            rpm=3,
            safety_margin_seconds=1.5,
        )
        self.assertAlmostEqual(wait, 11.5)

    def test_tpm_guard_waits_until_enough_tokens_expire(self):
        wait = MODULE.PersistentRateLimiter.compute_tpm_wait(
            [
                {"ts": 50.0, "tokens": 60},
                {"ts": 80.0, "tokens": 30},
            ],
            now=100.0,
            tpm=100,
            requested_tokens=30,
            safety_margin_seconds=1.5,
        )
        self.assertAlmostEqual(wait, 11.5)

    def test_rate_limiter_persists_request_timestamp(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            state = Path(temp_dir) / "rate.json"
            limiter = MODULE.PersistentRateLimiter(
                "tts:test",
                rpm=3,
                safety_margin_seconds=0.0,
                state_path=state,
                clock=lambda: 100.0,
                sleeper=lambda seconds: self.fail(f"unexpected sleep: {seconds}"),
            )
            waited = limiter.wait()
            data = MODULE.read_json(state, {})

        self.assertEqual(waited, 0.0)
        self.assertEqual(data["buckets"]["tts:test"], [100.0])

    def test_error_classification(self):
        self.assertEqual(
            MODULE.classify_api_error(
                RuntimeError("Error code: 403 - permission_denied: The caller does not have permission")
            ),
            "permission",
        )
        self.assertEqual(
            MODULE.classify_api_error(
                RuntimeError("Error code: 429 - RESOURCE_EXHAUSTED")
            ),
            "rate_limit",
        )
        self.assertEqual(
            MODULE.classify_api_error(
                RuntimeError("API_KEY_INVALID: API key not valid")
            ),
            "auth",
        )
        self.assertEqual(
            MODULE.classify_api_error(
                RuntimeError("Error code: 503 - service unavailable")
            ),
            "transient",
        )

    def test_provider_usage_extracts_audio_tokens(self):
        interaction = {
            "usage": {
                "total_input_tokens": 7,
                "total_output_tokens": 120,
                "total_tokens": 127,
                "input_tokens_by_modality": [
                    {"modality": "text", "tokens": 7}
                ],
                "output_tokens_by_modality": [
                    {"modality": "audio", "tokens": 120}
                ],
            }
        }
        usage = MODULE.extract_provider_usage(interaction, "Hello there.")

        self.assertEqual(usage["usage_source"], "provider")
        self.assertEqual(usage["total_input_tokens"], 7)
        self.assertEqual(usage["output_audio_tokens"], 120)
        self.assertEqual(usage["total_tokens"], 127)

    def test_provider_usage_falls_back_to_estimate(self):
        usage = MODULE.extract_provider_usage({}, "12345678")
        self.assertEqual(usage["usage_source"], "estimated")
        self.assertEqual(usage["estimated_input_tokens"], 2)

    def test_representative_rows_spread_across_sources(self):
        rows = [
            {
                "speaker": "mc",
                "status": "ready",
                "renpy_id": f"id_{index}",
                "id": f"id_{index}",
                "tts_text": "This is a useful representative line for testing selection.",
                "game_source_file": f"scene_{index}.rpy",
            }
            for index in range(12)
        ]
        selected = MODULE.representative_rows(rows, "mc", 5)

        self.assertEqual(len(selected), 5)
        self.assertEqual(len({row["id"] for row in selected}), 5)
        self.assertGreaterEqual(len({row["game_source_file"] for row in selected}), 4)

    def test_character_status_prioritizes_approval_and_aliases(self):
        self.assertEqual(
            MODULE.character_status(
                {
                    "enabled": True,
                    "voice_id": "voice_123",
                    "casting_status": "approved",
                }
            ),
            "APPROVED",
        )
        self.assertEqual(
            MODULE.character_status(
                {
                    "enabled": True,
                    "voice_ref": "mc",
                }
            ),
            "ALIAS->mc",
        )
        self.assertEqual(
            MODULE.character_status({"enabled": False}),
            "DISABLED",
        )

    def test_final_generation_plan_explains_missing_current_source(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "voice").mkdir(parents=True)
            (root / "original-source").mkdir(parents=True)
            (root / "voice" / "characters.json").write_text(
                __import__("json").dumps(
                    {
                        "schema_version": 1,
                        "characters": {
                            "jc": {
                                "display_name": "Jerk Cop",
                                "voice_id": "voice_test",
                                "voice_ref": "",
                                "enabled": True,
                                "line_count": 38,
                                "casting_status": "approved",
                                "profile": {
                                    "evidence_ids": ["sm1cs_dc009_3979a35b"]
                                },
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )
            (root / "original-source" / "SOURCE_COVERAGE.json").write_text(
                __import__("json").dumps(
                    {
                        "missing_paths": [
                            "code/scenes/character_scenes/dc/sm1cs-dc009.rpy",
                            "code/scenes/character_scenes/dc/sm1cs-dc009i.rpy",
                            "code/scenes/unrelated.rpy",
                        ]
                    }
                ),
                encoding="utf-8",
            )

            old_root = MODULE.ROOT
            old_vp_root = MODULE.vp.ROOT
            try:
                MODULE.ROOT = root
                MODULE.vp.ROOT = root
                studio = MODULE.VoiceStudio(
                    {
                        "characters_file": "voice/characters.json",
                        "wav_output_dir": "voice/generated/wav",
                    },
                    dict(MODULE.DEFAULT_RUNTIME_SETTINGS),
                )
                studio._manifest = []
                plan = studio.final_generation_plan("jc")
                summary = studio.describe_final_plan(plan)
            finally:
                MODULE.ROOT = old_root
                MODULE.vp.ROOT = old_vp_root

        self.assertEqual(len(plan["all_rows"]), 0)
        self.assertEqual(len(plan["eligible_rows"]), 0)
        self.assertEqual(plan["stored_line_count"], 38)
        self.assertEqual(
            plan["source_missing_hints"],
            [
                "code/scenes/character_scenes/dc/sm1cs-dc009.rpy",
                "code/scenes/character_scenes/dc/sm1cs-dc009i.rpy",
            ],
        )
        self.assertIn("Registry line_count: 38", summary)
        self.assertIn("sm1cs-dc009.rpy", summary)

    def test_final_generation_plan_counts_ready_and_pending_rows(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "voice").mkdir(parents=True)
            (root / "original-source").mkdir(parents=True)
            (root / "voice" / "characters.json").write_text(
                __import__("json").dumps(
                    {
                        "schema_version": 1,
                        "characters": {
                            "mc": {
                                "display_name": "Mike",
                                "voice_id": "voice_test",
                                "voice_ref": "",
                                "enabled": True,
                                "line_count": 2,
                                "casting_status": "approved",
                                "profile": {},
                            }
                        },
                    }
                ),
                encoding="utf-8",
            )
            (root / "original-source" / "SOURCE_COVERAGE.json").write_text(
                '{"missing_paths":[]}',
                encoding="utf-8",
            )

            old_root = MODULE.ROOT
            old_vp_root = MODULE.vp.ROOT
            try:
                MODULE.ROOT = root
                MODULE.vp.ROOT = root
                studio = MODULE.VoiceStudio(
                    {
                        "characters_file": "voice/characters.json",
                        "wav_output_dir": "voice/generated/wav",
                    },
                    dict(MODULE.DEFAULT_RUNTIME_SETTINGS),
                )
                studio._manifest = [
                    {
                        "id": "line_1",
                        "speaker": "mc",
                        "status": "ready",
                        "renpy_id": "line_1",
                        "review_reasons": [],
                    },
                    {
                        "id": "line_2",
                        "speaker": "mc",
                        "status": "needs_review",
                        "renpy_id": "",
                        "review_reasons": ["renpy-id-not-resolved"],
                    },
                ]
                plan = studio.final_generation_plan("mc")
            finally:
                MODULE.ROOT = old_root
                MODULE.vp.ROOT = old_vp_root

        self.assertEqual(len(plan["all_rows"]), 2)
        self.assertEqual(len(plan["eligible_rows"]), 1)
        self.assertEqual(len(plan["pending_rows"]), 1)
        self.assertEqual(plan["missing_renpy_id_count"], 1)
        self.assertEqual(plan["review_reasons"]["renpy-id-not-resolved"], 1)

    def test_non_idempotent_create_does_not_retry_transient_errors(self):
        class FakeLimiter:
            rpm = 3
            safety_margin_seconds = 1.5

            def wait(self, estimated_tokens=0):
                return 0.0

        attempts = 0

        def fail():
            nonlocal attempts
            attempts += 1
            raise RuntimeError("Error code: 503 - unavailable")

        with self.assertRaises(RuntimeError):
            MODULE.api_call_with_retry(
                fail,
                limiter=FakeLimiter(),
                settings=MODULE.DEFAULT_RUNTIME_SETTINGS,
                label="create voice",
                idempotent=False,
            )
        self.assertEqual(attempts, 1)

    def test_idempotent_permission_error_retries(self):
        class FakeLimiter:
            rpm = 3
            safety_margin_seconds = 1.5

            def wait(self, estimated_tokens=0):
                return 0.0

        attempts = 0

        def sometimes_fail():
            nonlocal attempts
            attempts += 1
            if attempts == 1:
                raise RuntimeError(
                    "Error code: 403 - permission_denied: The caller does not have permission"
                )
            return "ok"

        settings = dict(MODULE.DEFAULT_RUNTIME_SETTINGS)
        settings["max_retries"] = 2
        settings["permission_retry_delay_seconds"] = 0.0
        settings["retry_base_delay_seconds"] = 0.0

        with mock.patch.object(MODULE.time, "sleep", return_value=None):
            result, _ = MODULE.api_call_with_retry(
                sometimes_fail,
                limiter=FakeLimiter(),
                settings=settings,
                label="tts",
                idempotent=True,
                retry_permission=True,
            )

        self.assertEqual(result, "ok")
        self.assertEqual(attempts, 2)


if __name__ == "__main__":
    unittest.main()
