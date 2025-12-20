from app.pipeline.findings import Finding

def run_correctness_checks(diffs):
    findings = []
    for d in diffs:
        if "items[0]" in d:
            findings.append(Finding(
                category="Correctness",
                subtype="BoundaryCheck",
                severity="High",
                fix_scope="Local",
                message="Accessing first element without checking for empty list."
            ))
    return findings
