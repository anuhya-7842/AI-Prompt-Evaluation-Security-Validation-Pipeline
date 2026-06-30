import streamlit as st
import pandas as pd
import json

st.set_page_config(page_title="LLM Evaluation Dashboard", layout="wide")

st.title("📊 LLM Evaluation Dashboard")

# Load Promptfoo results
with open("../results.json", "r") as f:
    data = json.load(f)

results = data["results"]["results"]

rows = []

for result in results:
    rows.append({
        "Question": result["vars"]["vars.question"],
        "Expected": result["vars"]["assert[0].value"],
        "Actual": result["response"]["output"],
        "Latency": result["latencyMs"],
        "Pass": result["success"]
    })

df = pd.DataFrame(rows)

# -----------------------
# Metrics
# -----------------------

total = len(df)
passed = df["Pass"].sum()
failed = total - passed

pass_rate = (passed / total) * 100
hallucination_rate = (failed / total) * 100

avg_latency = df["Latency"].mean()
p50_latency = df["Latency"].median()
p95_latency = df["Latency"].quantile(0.95)

estimated_cost = total * 0.00002

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tests", total)
col2.metric("Passed", passed)
col3.metric("Failed", failed)
col4.metric("Pass Rate", f"{pass_rate:.2f}%")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Hallucination Rate", f"{hallucination_rate:.2f}%")
col2.metric("Average Latency", f"{avg_latency:.2f} ms")
col3.metric("P50 Latency", f"{p50_latency:.2f} ms")
col4.metric("P95 Latency", f"{p95_latency:.2f} ms")

st.metric("Estimated Cost", f"${estimated_cost:.5f}")

st.divider()

# -----------------------
# Charts
# -----------------------

st.subheader("Pass / Fail Distribution")

pass_counts = df["Pass"].value_counts()

st.bar_chart(pass_counts)

st.subheader("Latency per Test")

latency_df = df[["Latency"]]

st.line_chart(latency_df)

st.subheader("Detailed Results")

st.dataframe(df, use_container_width=True)