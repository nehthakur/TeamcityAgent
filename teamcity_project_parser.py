import re


def parse_project_name(content):

    match = re.search(
        r'name\s*=\s*"([^"]+)"',
        content
    )

    if match:
        return match.group(1)

    return "Unknown Project"


def parse_build_configurations(content):

    names = re.findall(
        r'name\s*=\s*"([^"]+)"',
        content
    )

    project_name = parse_project_name(content)

    builds = []

    for name in names:

        if name != project_name:

            builds.append(name)

    return builds
