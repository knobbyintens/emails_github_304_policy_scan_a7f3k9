# Policy Scan

Automated open-source licence auditing for large monorepos.

**Status: Released — v2.1.1 (2025-08-18).** This repository contains the production
scanner and the rule set described in the showcase entry.

## Contents

- `policy_scan/scanner.py` — lockfile and vendored-tree crawler
- `policy_scan/rules.py` — licence obligation rule engine
- `policy_scan/report.py` — team-grouped report rendering
- `tests/test_scanner.py` — fixture-based scanner tests

## Usage

```
pip install -e .
policy-scan --root . --policy policy.yaml
```

## Licence

Apache-2.0.
