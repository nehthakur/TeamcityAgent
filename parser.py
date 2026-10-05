import re


def parse_teamcity_dsl(content):

    build_names = re.findall(
        r'name\s*=\s*"([^"]+)"',
        content
    )

    triggers = []

    if "vcs {" in content:
        triggers.append("VCS Trigger")

    if "schedule {" in content:
        triggers.append("Schedule Trigger")

    if "finishBuildTrigger" in content:
        triggers.append("Finish Build Trigger")

    steps = []

    if "maven {" in content:
        steps.append("Maven")

    if "gradle {" in content:
        steps.append("Gradle")

    if "dockerCommand {" in content:
        steps.append("Docker")

    if "dotnetBuild {" in content:
        steps.append(".NET Build")

    dependencies = []

    snapshot_matches = re.findall(
        r'snapshot\((.*?)\)',
        content
    )

    for dep in snapshot_matches:

        dependencies.append(
            f"Snapshot Dependency -> {dep}"
        )

    parameters = re.findall(
        r'param\(\s*"([^"]+)"',
        content
    )

    requirements = re.findall(
        r'equals\(\s*"([^"]+)"',
        content
    )

    return {
        "build_names": build_names,
        "triggers": triggers,
        "steps": steps,
        "dependencies": dependencies,
        "parameters": parameters,
        "requirements": requirements
    }


def explain_pipeline(parsed):

    explanations = []

    build_count = len(parsed["build_names"])

    if build_count > 0:
        build_count -= 1

    explanations.append(
        f"Pipeline contains {build_count} build configuration(s)."
    )

    if parsed["triggers"]:

        explanations.append(
            f"Pipeline starts using: {', '.join(parsed['triggers'])}."
        )

    if "Maven" in parsed["steps"]:

        explanations.append(
            "This appears to be a Java/Maven project."
        )

    if "adle" in parsed["steps"]:

        explanations.append(
            "This appears to be a Java/Gradle project."
        )

    if "Docker" in parsed["steps"]:

        explanations.append(
            "Pipeline performs Docker operations."
        )

    if parsed["dependencies"]:

        explanations.append(
            f"Pipeline contains {len(parsed['dependencies'])} dependency configuration(s)."
        )

    else:

        explanations.append(
            "This build executes independently without declared dependencies."
        )

    if parsed["requirements"]:

        explanations.append(
            "Pipeline contains agent requirements and may run only on specific build agents."
        )

    return explanations
