"""Licence obligation rule engine."""

ALLOWED_OBLIGATIONS = {"notice", "attribution", "none"}
BLOCKING_LICENCES = {"AGPL-3.0", "GPL-3.0"}


def evaluate(licence_id: str, distribution_policy: dict) -> dict:
    if licence_id in distribution_policy.get("blocked_licences", BLOCKING_LICENCES):
        return {"licence": licence_id, "verdict": "block", "reason": "incompatible with distribution"}
    return {"licence": licence_id, "verdict": "allow", "reason": "obligations satisfied"}
