def calculate_score(findings):

    score = 100

    for finding in findings:

        severity = finding["severity"]

        if severity == "HIGH":
            score -= 20

        elif severity == "MEDIUM":
            score -= 10

        elif severity == "LOW":
            score -= 5

    return max(score, 0)
