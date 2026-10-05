import re


def discover_flow(content):

    dependencies = re.findall(
        r'snapshot\((.*?)\)',
        content
    )

    flow = []

    for dep in dependencies:
        flow.append(dep.strip())

    return flow
