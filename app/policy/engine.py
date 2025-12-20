import yaml
from pathlib import Path

POLICY_FILE = Path("policy.yaml")

def apply_policies(findings):
    policies = yaml.safe_load(POLICY_FILE.read_text())
    actions = []

    for f in findings:
        for p in policies["policies"]:
            when = p["when"]
            if when.get("category") and when["category"] != f.category:
                continue
            if when.get("severity") and when["severity"] != f.severity:
                continue
            if when.get("fix_scope") and when["fix_scope"] != f.fix_scope:
                continue
            if when.get("context"):
                if not all(f.context.get(k) == v for k, v in when["context"].items()):
                    continue
            actions.append({
                "finding": f.subtype,
                "action": p["action"]
            })
            break
    return actions
