import streamlit as st

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

st.info(f"Current mode: {mode}")
