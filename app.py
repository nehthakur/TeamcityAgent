import streamlit as st

from parser import (
    parse_teamcity_dsl,
    explain_pipeline
)

from report_generator import (
    generate_project_summary
)

from rules import analyze_risks
from scoring import calculate_score

from pipeline_analyzer import generate_overview
from flow_analyzer import discover_flow

from architecture_analyzer import (
    analyze_architecture
)

from project_parser import extract_project

from teamcity_project_parser import (
    parse_project_name,
    parse_build_configurations
)

from dependency_graph import (
    build_dependency_graph
)

from execution_order import (
    generate_execution_order
)


st.set_page_config(
    page_title="TeamCity Pipeline Understanding Assistant",
    layout="wide"
)

st.title(
    "🚀 TeamCity Pipeline Understanding Assistant"
)

uploaded_file = st.file_uploader(
    "Upload TeamCity Project ZIP",
    type=["zip"]
)

if uploaded_file:

    content = extract_project(
        uploaded_file
    )

    project_name = parse_project_name(
        content
    )

    build_configs = parse_build_configurations(
        content
    )

    parsed = parse_teamcity_dsl(
        content
    )

    overview = generate_overview(
        parsed,
        build_configs
    )

    flow = discover_flow(
        content
    )

    graph = build_dependency_graph(
        content
    )

    execution_order = generate_execution_order(
        graph
    )

    architecture = analyze_architecture(
        build_configs,
        parsed
    )
    
    report = generate_project_summary(
    	project_name,
    	overview,
    	architecture,
    	execution_order,
    	parsed
    )    

    explanations = explain_pipeline(
        parsed
    )

    risks = analyze_risks(
        content
    )

    score = calculate_score(
        risks
    )

    # ==========================================
    # Dependency Graph
    # ==========================================

    st.header("🕸️ Dependency Graph")

    st.json(graph)

    # ==========================================
    # Project Information
    # ==========================================

    st.header("📦 Project Information")

    st.write(
        f"Project Name: {project_name}"
    )

    st.subheader(
        "Build Configurations"
    )

    for build in build_configs:

        st.write(
            f"• {build}"
        )
    
    st.header("📄 Architecture Report")

    st.write(
    	f"**Project:** "
    	f"{report['project_name']}"
    )

    st.write(
    	f"**Pipeline Type:** "
    	f"{report['pipeline_type']}"
    )

    st.write(
    	f"**Execution Model:** "
    	f"{report['execution_model']}"
    )

    st.write(
    	f"**Start Stage:** "
    	f"{report['start_stage']}"
    )

    st.write(
    	f"**End Stage:** "
    	f"{report['end_stage']}"
    )

    st.write(
    	f"**Build Configurations:** "
    	f"{report['build_count']}"
    )

    st.write(
    	f"**Dependencies:** "
    	f"{report['dependency_count']}"
    )

    st.write(
    	f"**Technology:** "
    	f"{', '.join(report['technology'])}"
    )

    if report["requirements"]:

    	st.write(
        	f"**Requirements:** "
        	f"{', '.join(report['requirements'])}"
    	)

    # ==========================================
    # Pipeline Overview
    # ==========================================

    st.header("🏗️ Pipeline Overview")

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            f"**Pipeline Type:** "
            f"{overview['pipeline_type']}"
        )

        st.write(
            f"**Technology Stack:** "
            f"{', '.join(overview['technology'])}"
        )

        st.write(
            f"**Complexity:** "
            f"{overview['complexity']}"
        )

    with col2:

        st.write(
            f"**Build Configurations:** "
            f"{overview['build_count']}"
        )

        st.write(
            f"**Dependencies:** "
            f"{overview['dependency_count']}"
        )

    # ==========================================
    # Execution Order
    # ==========================================

    st.header("🚦 Execution Order")

    for item in execution_order:

        st.write(
            f"✅ {item}"
        )

    # ==========================================
    # Pipeline Flow
    # ==========================================

    st.header("🔀 Pipeline Flow")

    for index, stage in enumerate(
        execution_order
    ):

        st.write(stage)

        if index < len(execution_order) - 1:

            st.write("↓")

    # ==========================================
    # Architecture Analysis
    # ==========================================

    st.header("🏛️ Architecture Analysis")

    st.write(
        f"**Execution Model:** "
        f"{architecture['execution_model']}"
    )

    st.write(
        f"**Stages:** "
        f"{len(architecture['stages'])}"
    )

    for stage in architecture["stages"]:

        st.write(
            f"• {stage}"
        )

    # ==========================================
    # Pipeline Summary
    # ==========================================

    st.header("📋 Pipeline Summary")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Build Names")

        st.write(
            parsed["build_names"]
        )

        st.subheader("Triggers")

        st.write(
            parsed["triggers"]
        )

        st.subheader("Build Steps")

        st.write(
            parsed["steps"]
        )

    with col2:

        st.subheader("Dependencies")

        st.write(
            parsed["dependencies"]
        )

        st.subheader("Parameters")

        st.write(
            parsed["parameters"]
        )

        st.subheader("Agent Requirements")

        st.write(
            parsed["requirements"]
        )

    # ==========================================
    # Pipeline Understanding
    # ==========================================

    st.header("🧠 Pipeline Understanding")

    if explanations:

    	for item in explanations:
        	st.success(item)

    else:

   	 st.warning(
        	"No pipeline understanding information available."
    )

    # ==========================================
    # Health Score
    # ==========================================

    st.header("📊 Health Score")

    st.metric(
        label="Pipeline Health Score",
        value=f"{score}/100"
    )

    # ==========================================
    # Risk Analysis
    # ==========================================

    st.header("⚠️ Risk Analysis")

    if len(risks) == 0:

        st.success(
            "No risks detected."
        )

    else:

        for risk in risks:

            message = (
                f"{risk['issue']}\n\n"
                f"Recommendation: "
                f"{risk['recommendation']}"
            )

            if risk["severity"] == "HIGH":

                st.error(message)

            elif risk["severity"] == "MEDIUM":

                st.warning(message)

            elif risk["severity"] == "LOW":

                st.info(message)

            else:

                st.write(message)

    st.success(
        "Pipeline analysis completed successfully."
    )
