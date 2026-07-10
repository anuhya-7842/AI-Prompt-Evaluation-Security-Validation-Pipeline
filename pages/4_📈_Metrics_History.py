import streamlit as st
import pandas as pd

st.set_page_config(page_title="Metrics History", page_icon="📈")

st.title("📈 Metrics History")

history = pd.read_csv("history/metrics_history.csv")

st.dataframe(history, use_container_width=True)

history["PassRate"] = (
    history["Passed"] / history["TotalTests"]
) * 100

st.subheader("Pass Rate")
st.line_chart(history.set_index("Timestamp")["PassRate"])

st.subheader("Hallucination Rate")
st.line_chart(history.set_index("Timestamp")["HallucinationRate"])

st.subheader("Average Latency")
st.line_chart(history.set_index("Timestamp")["AverageLatency"])

st.subheader("P95 Latency")
st.line_chart(history.set_index("Timestamp")["P95Latency"])