"""Team-grouped report rendering."""


def render(team_owners, findings):
    sections = {}
    for finding in findings:
        team = team_owners.get(finding["package"], "unassigned")
        sections.setdefault(team, []).append(finding)
    lines = []
    for team, items in sorted(sections.items()):
        lines.append(f"## {team}")
        for item in items:
            lines.append(f"- {item['package']}: {item['verdict']} ({item['reason']})")
    return "\n".join(lines)
