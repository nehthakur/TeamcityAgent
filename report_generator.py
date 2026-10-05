def generate_project_summary(
    project_name,
    overview,
    architecture,
    execution_order,
    parsed
):

    report = {}

    report["project_name"] = project_name

    report["pipeline_type"] = overview[
        "pipeline_type"
    ]

    report["execution_model"] = architecture[
        "execution_model"
    ]

    report["build_count"] = overview[
        "build_count"
    ]

    report["dependency_count"] = overview[
        "dependency_count"
    ]

    report["technology"] = overview[
        "technology"
    ]

    report["requirements"] = parsed[
        "requirements"
    ]

    if execution_order:

        report["start_stage"] = execution_order[0]

        report["end_stage"] = execution_order[-1]

    else:

        report["start_stage"] = "Unknown"

        report["end_stage"] = "Unknown"

    return report
