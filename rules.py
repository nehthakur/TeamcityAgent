import re


def analyze_risks(content):

    findings = []

    # Timeout
    if "executionTimeoutMin" not in content:
        findings.append({
            "severity": "MEDIUM",
            "issue": "Build timeout not configured",
            "recommendation": "Configure executionTimeoutMin to prevent long-running builds."
        })

    # Branch Filter
    if "branchFilter" not in content:
        findings.append({
            "severity": "LOW",
            "issue": "Branch filter not configured",
            "recommendation": "Limit builds to relevant branches."
        })

    # Retry Policy
    if "retryBuild" not in content:
        findings.append({
            "severity": "LOW",
            "issue": "Retry policy not configured",
            "recommendation": "Add retry policy for transient failures."
        })

    # Hardcoded password detection
    if "password(" in content:
        findings.append({
            "severity": "HIGH",
            "issue": "Possible hardcoded password detected",
            "recommendation": "Use TeamCity secure parameters."
        })

    # Agent Requirements
    if "requirements {" in content:
        findings.append({
            "severity": "INFO",
            "issue": "Agent requirements detected",
            "recommendation": "Verify compatible agents are available."
        })

    return findings

