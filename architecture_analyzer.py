def analyze_architecture(build_configs, parsed):

    architecture = {}

    build_count = len(build_configs)
    dependency_count = len(parsed["dependencies"])

    architecture["build_count"] = build_count
    architecture["dependency_count"] = dependency_count

    if dependency_count == 0:
        architecture["execution_model"] = "Standalone"

    elif dependency_count < build_count:
        architecture["execution_model"] = "Linear"

    else:
        architecture["execution_model"] = "Complex"

    architecture["stages"] = build_configs

    return architecture
