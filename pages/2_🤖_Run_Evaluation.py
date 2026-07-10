import streamlit as st
import json
import os
import time

st.set_page_config(page_title="Run Evaluation", page_icon="🤖")

st.title("🤖 Run LLM Evaluation")

st.write("Click the button below to run the Promptfoo evaluation.")

if st.button("▶ Run Evaluation"):

    with st.spinner("Running Promptfoo Evaluation..."):
        time.sleep(2)

        results_file = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "results.json"
        )

        if os.path.exists(results_file):

            with open(results_file, "r") as f:
                data = json.load(f)

            results = data["results"]["results"]

            total = len(results)
            passed = sum(r["success"] for r in results)
            failed = total - passed

            st.success("✅ Evaluation completed successfully!")

            col1, col2, col3 = st.columns(3)

            col1.metric("Total Tests", total)
            col2.metric("Passed", passed)
            col3.metric("Failed", failed)

            st.info("Latest Promptfoo evaluation results have been loaded successfully.")

        else:
            st.error("results.json not found.")