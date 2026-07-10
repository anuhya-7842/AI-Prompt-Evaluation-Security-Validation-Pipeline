import streamlit as st

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="LLM Evaluation Pipeline",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# Header
# ----------------------------
st.title("🤖 LLM Evaluation CI/CD Pipeline")
st.markdown("### Automated Evaluation Pipeline for Large Language Models")

st.write("""
Welcome to the **LLM Evaluation Pipeline Dashboard**.

This project demonstrates an automated evaluation system for Large Language Models (LLMs).
It evaluates AI-generated responses using **Promptfoo** and **Google Gemini**, measures key
performance metrics, and visualizes the results through an interactive dashboard.
""")

st.divider()

# ----------------------------
# Features & Tech Stack
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🚀 Project Features")

    st.markdown("""
- ✅ Automated LLM Evaluation
- ✅ Golden Dataset Testing
- ✅ Promptfoo Integration
- ✅ Google Gemini API
- ✅ Hallucination Detection
- ✅ Response Quality Evaluation
- ✅ Latency Monitoring
- ✅ Metrics History Tracking
- ✅ Interactive Dashboard
- ✅ GitHub Actions CI/CD
""")

with col2:
    st.subheader("🛠 Technology Stack")

    st.markdown("""
- Python
- Streamlit
- Promptfoo
- Google Gemini
- GitHub Actions
- Pandas
- JSON
- CSV
""")

st.divider()

# ----------------------------
# Workflow
# ----------------------------
st.subheader("📈 Project Workflow")

st.code("""
Golden Dataset
      │
      ▼
Promptfoo Evaluation
      │
      ▼
Google Gemini
      │
      ▼
Evaluation Results
      │
      ▼
Metrics Calculation
      │
      ▼
Dashboard & History
      │
      ▼
GitHub Actions CI/CD
""")

st.divider()

# ----------------------------
# Metrics
# ----------------------------
st.subheader("📊 What This Project Measures")

m1, m2, m3 = st.columns(3)

m1.metric("Hallucination Detection", "✔")
m2.metric("Latency Monitoring", "✔")
m3.metric("Pass/Fail Evaluation", "✔")

m4, m5, m6 = st.columns(3)

m4.metric("Prompt Evaluation", "✔")
m5.metric("Golden Dataset Testing", "✔")
m6.metric("CI/CD Automation", "✔")

st.divider()

# ----------------------------
# Navigation
# ----------------------------
st.subheader("📂 Explore the Project")

st.info("""
Use the left sidebar to navigate through the application.

🏠 Home

📁 Golden Dataset

🤖 Run Evaluation

📊 Dashboard

📈 Metrics History

ℹ️ Project Information
""")

st.divider()

# ----------------------------
# Recruiter Section
# ----------------------------
st.subheader("🎯 Why This Project Matters")

st.write("""
Modern AI applications require continuous monitoring to ensure they remain accurate,
reliable, and free from hallucinations.

This project demonstrates a production-style evaluation pipeline that automatically:

- Executes evaluation tests on every update
- Measures response quality
- Detects hallucinations
- Tracks latency trends
- Stores evaluation history
- Visualizes metrics in real time
- Integrates with GitHub Actions for CI/CD

It showcases practical skills in **Generative AI, Prompt Engineering, LLM Evaluation,
Python, Streamlit, GitHub Actions, and Google Gemini API**.
""")

st.success("✅ End-to-End LLM Evaluation Pipeline Successfully Demonstrated")