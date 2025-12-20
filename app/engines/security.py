from app.pipeline.findings import Finding

def run_security_checks(diffs):
    findings = []
    for d in diffs:
        if "SELECT" in d and "+" in d:
            findings.append(Finding(
                category="Security",
                subtype="UnsafeInputHandling",
                severity="High",
                fix_scope="Local",
                message="Possible SQL injection due to string concatenation."
            ))
    return findings
