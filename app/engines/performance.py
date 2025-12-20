from app.pipeline.findings import Finding

def run_performance_checks(diffs):
    findings = []
    for d in diffs:
        if "for" in d and "db." in d:
            findings.append(Finding(
                category="Performance",
                subtype="HotPathDegradation",
                severity="High",
                fix_scope="Architectural",
                message="Database call inside frequently executed loop.",
                context={"hot_path": True}
            ))
    return findings
