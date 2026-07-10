import streamlit as st
import subprocess
import os

st.set_page_config(page_title="Run Evaluation", page_icon="🤖")

st.title("🤖 Run LLM Evaluation")

st.write("Click the button below to run the Promptfoo evaluation.")

if st.button("▶ Run Evaluation"):

    with st.spinner("Running Promptfoo Evaluation..."):

        result = subprocess.run(
            ["cmd", "/c", "npx", "promptfoo", "eval", "--output", "results.json"],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.dirname(__file__))
        )

    if result.returncode == 0:
        st.success("✅ Evaluation completed successfully!")
        st.text(result.stdout)
    else:
        st.error("❌ Evaluation failed!")
        st.text(result.stderr)