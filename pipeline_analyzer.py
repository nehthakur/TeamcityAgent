def determine_pipeline_type(parsed):

    build_names = " ".join(parsed["build_names"])

    if "deploy" in build_names.lower():
        return "CI/CD Pipeline"

    return "CI Pipeline"


def determine_technology(parsed):

    tech = []

    if "Maven" in parsed["steps"]:
        tech.extend(["Java", "Maven"])

    if "Gradle" in parsed["steps"]:
        tech.extend(["Java", "Gradle"])

    if "Docker" in parsed["steps"]:
        tech.append("Docker")

    if ".NET Build" in parsed["steps"]:
        tech.append(".NET")

    if not tech:
        tech.append("Unknown")

    return list(set(tech))


def determine_complexity(parsed):

    score = (
        len(parsed["build_names"])
        + len(parsed["steps"])
        + len(parsed["dependencies"])
    )

    if score <= 3:
        return "Low"

    elif score <= 8:
        return "Medium"

    return "High"


def generate_overview(parsed, build_configs):

    return {
        "pipeline_type": determine_pipeline_type(parsed),
        "technology": determine_technology(parsed),
        "complexity": determine_complexity(parsed),
        "build_count": len(build_configs),
        "dependency_count": len(parsed["dependencies"])
    }
