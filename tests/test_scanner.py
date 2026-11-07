import json
from pathlib import Path

from policy_scan.scanner import scan_lockfile


def test_scan_lockfile(tmp_path: Path):
    lock = tmp_path / "deps.json"
    lock.write_text(json.dumps({"packages": {"alpha": {"version": "1.0.0"}}}), encoding="utf-8")
    result = scan_lockfile(lock)
    assert result == [{"name": "alpha", "version": "1.0.0"}]
