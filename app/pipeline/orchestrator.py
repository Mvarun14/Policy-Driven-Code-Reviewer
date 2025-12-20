from app.engines.correctness import run_correctness_checks
from app.engines.performance import run_performance_checks
from app.engines.security import run_security_checks
from app.policy.engine import apply_policies

def run_pipeline(payload):
    diffs = payload.get("diffs", [])
    findings = []
    findings += run_correctness_checks(diffs)
    findings += run_performance_checks(diffs)
    findings += run_security_checks(diffs)
    decisions = apply_policies(findings)
    return {
        "findings": [f.__dict__ for f in findings],
        "decisions": decisions
    }
