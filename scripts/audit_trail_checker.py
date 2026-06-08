# audit_trail_checker.py
# FDA 21 CFR Part 11 Audit Trail Validator
# Author: Sneha Ajmira

import argparse
import csv
import json
import logging
from datetime import datetime
from typing import List, Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

REQUIRED_FIELDS = [
    "timestamp", "user_id", "action_type",
    "record_id", "field_name", "old_value",
    "new_value", "reason_for_change",
]


def parse_log(filepath: str) -> List[Dict]:
    if filepath.endswith(".csv"):
        with open(filepath, newline="") as f:
            return list(csv.DictReader(f))
    with open(filepath) as f:
        return json.load(f)


def validate_entry(entry: Dict) -> List[str]:
    violations = []
    for field in REQUIRED_FIELDS:
        val = entry.get(field, "").strip()
        if not val or val.lower() in ("null", "none", "n/a", ""):
            violations.append(f"Missing: {field}")
    reason = entry.get("reason_for_change", "").lower()
    if reason in {"test", "n/a", "none", "tbd", ""}:
        violations.append("Generic reason for change not acceptable")
    return violations


def run_check(entries: List[Dict]) -> dict:
    valid, errors = 0, []
    for i, e in enumerate(entries):
        v = validate_entry(e)
        if v:
            errors.append({"row": i+1, "id": e.get("record_id", "?"), "issues": v})
        else:
            valid += 1
    n = len(entries)
    return {"total": n, "valid": valid, "invalid": len(errors),
            "score": round(valid/n*100, 2) if n else 0, "errors": errors}


def save_report(results: dict, path: str) -> None:
    with open(path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["21 CFR Part 11 Audit Trail Report"])
        w.writerow(["Generated:", datetime.utcnow().isoformat()])
        w.writerow([])
        w.writerow(["Total", results["total"]])
        w.writerow(["Valid", results["valid"]])
        w.writerow(["Score", f"{results['score']}%"])
        if results["errors"]:
            w.writerow([])
            w.writerow(["Row", "Record ID", "Issues"])
            for e in results["errors"]:
                w.writerow([e["row"], e["id"], "; ".join(e["issues"])])
    logger.info(f"Report: {path}")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--log-file", required=True)
    p.add_argument("--report", default="audit_report.csv")
    args = p.parse_args()
    entries = parse_log(args.log_file)
    results = run_check(entries)
    logger.info(f"Score: {results['score']}%")
    save_report(results, args.report)


if __name__ == "__main__":
    main()
