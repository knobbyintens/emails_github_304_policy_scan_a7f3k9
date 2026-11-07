"""Dependency crawler for Policy Scan."""

import json
from pathlib import Path
from typing import Dict, List


def scan_lockfile(path: Path) -> List[Dict[str, str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    packages = []
    for name, meta in data.get("packages", {}).items():
        packages.append({"name": name, "version": meta.get("version", "unknown")})
    return packages


def scan_vendored(root: Path) -> List[Dict[str, str]]:
    found = []
    for licence in root.glob("vendor/**/LICENCE*"):
        found.append({"name": licence.parent.name, "licence_file": str(licence)})
    return found
