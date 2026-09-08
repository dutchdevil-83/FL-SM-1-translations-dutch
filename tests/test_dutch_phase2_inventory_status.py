import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "dutch_phase0_inventory.py"
SPEC = importlib.util.spec_from_file_location("dutch_phase0_inventory_phase2", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class Phase2InventoryStatusTests(unittest.TestCase):
    def test_committed_target_promotes_default_status_to_review(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = root / "dutch" / "code" / "classes" / "character.rpy"
            target.parent.mkdir(parents=True)
            target.write_text("translate dutch strings:\n", encoding="utf-8")

            status, notes = MODULE.promote_committed_target(
                root,
                "dutch",
                "code/classes/character.rpy",
                "not started",
                "",
                "not started",
            )

        self.assertEqual(status, "review")
        self.assertEqual(notes, MODULE.AUTO_REVIEW_NOTE)

    def test_existing_manual_status_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            target = root / "dutch" / "code" / "classes" / "character.rpy"
            target.parent.mkdir(parents=True)
            target.write_text("translate dutch strings:\n", encoding="utf-8")

            status, notes = MODULE.promote_committed_target(
                root,
                "dutch",
                "code/classes/character.rpy",
                "in progress",
                "manual note",
                "not started",
            )

        self.assertEqual(status, "in progress")
        self.assertEqual(notes, "manual note")

    def test_missing_target_does_not_promote_status(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            status, notes = MODULE.promote_committed_target(
                Path(temp_dir),
                "dutch",
                "code/classes/character.rpy",
                "not started",
                "",
                "not started",
            )

        self.assertEqual(status, "not started")
        self.assertEqual(notes, "")


if __name__ == "__main__":
    unittest.main()
