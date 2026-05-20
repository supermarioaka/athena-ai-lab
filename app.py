import streamlit as st
from src.problem_analyzer import analyze_problem

st.set_page_config(page_title="Athena AI Lab", page_icon="🧠", layout="wide")

st.title("🧠 Athena AI Lab")

st.write("AI Mathematical Reasoning & Decision Lab")

mode = st.selectbox(
    "Choose mode",
    [
        "Mathematical Reasoning",
        "Statistics",
        "Simulations",
        "Explainability",
        "Decision Support",
        "Research Workflow",
    ],
)

problem_text = st.text_area(
    "Write a mathematical, statistical, or research problem",
    height=180,
    placeholder="Example: Given a Markov chain with transition matrix P, determine whether it has a stationary distribution.",
)

if st.button("Analyze Problem"):
    if problem_text.strip() == "":
        st.warning("Please write a problem first.")
    else:
        analysis = analyze_problem(problem_text, mode)

        st.subheader("Athena Analysis")

        st.markdown("### Problem Type")
        st.write(analysis["problem_type"])

        st.markdown("### Given Information")
        st.write(analysis["given_information"])

        st.markdown("### Unknown / Goal")
        st.write(analysis["unknown_goal"])

        st.markdown("### Suggested Approach")
        st.write(analysis["suggested_approach"])
