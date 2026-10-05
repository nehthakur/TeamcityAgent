import re


def build_dependency_graph(content):

    graph = {}

    builds = re.findall(
        r'object\s+(\w+)\s*:\s*BuildType',
        content
    )

    for build in builds:
        graph[build] = []

    matches = re.findall(
        r'object\s+(\w+)\s*:\s*BuildType\(\{(.*?)\}\)',
        content,
        re.DOTALL
    )

    for build_name, block in matches:

        deps = re.findall(
            r'snapshot\((\w+)\)',
            block
        )

        graph[build_name] = deps

    return graph
