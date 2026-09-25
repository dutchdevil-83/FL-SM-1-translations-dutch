import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IMPORTER = ROOT / "tools" / "Import-OriginalGameVoiceSource.ps1"


class VoiceImporterSyntaxTests(unittest.TestCase):
    def test_branch_name_before_colon_uses_braced_interpolation(self):
        source = IMPORTER.read_text(encoding="utf-8")

        self.assertIn("${BranchName}:", source)
        self.assertNotIn("$BranchName:", source)


if __name__ == "__main__":
    unittest.main()
