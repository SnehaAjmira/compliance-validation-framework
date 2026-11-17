import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_trail_checker import parse_log, run_check, validate_entry  # noqa: E402

GOOD = {
    "timestamp": "2026-03-02T09:40:05", "user_id": "jdoe", "action_type": "UPDATE",
    "record_id": "SMP-1", "field_name": "result", "old_value": "1", "new_value": "2",
    "reason_for_change": "Transcription error corrected",
}


class TestAuditTrail(unittest.TestCase):
    def test_compliant_entry(self):
        self.assertEqual(validate_entry(GOOD), [])

    def test_create_allows_blank_old_value(self):
        self.assertEqual(validate_entry({**GOOD, "action_type": "CREATE", "old_value": ""}), [])

    def test_missing_user(self):
        self.assertIn("Missing user_id", validate_entry({**GOOD, "user_id": ""}))

    def test_generic_reason(self):
        self.assertIn("Reason for change is generic", validate_entry({**GOOD, "reason_for_change": "TBD"}))

    def test_bad_timestamp(self):
        self.assertIn("Timestamp not in ISO 8601 format", validate_entry({**GOOD, "timestamp": "03/02/2026"}))

    def test_none_values_from_json(self):
        self.assertIn("Missing user_id", validate_entry({**GOOD, "user_id": None}))

    def test_sample_file(self):
        results = run_check(parse_log(str(ROOT / "examples" / "sample_audit_trail.csv")))
        self.assertEqual((results["total"], results["valid"]), (8, 3))


if __name__ == "__main__":
    unittest.main()
