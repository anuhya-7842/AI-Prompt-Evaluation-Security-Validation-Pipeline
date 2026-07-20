# LLM Evaluation CI/CD Pipeline

## Overview

This project implements an end-to-end LLM Evaluation Pipeline that automatically evaluates Large Language Model (LLM) responses using Promptfoo and Google Gemini. It measures response quality, tracks evaluation metrics over time, and visualizes results through a Streamlit dashboard.

The pipeline integrates GitHub Actions CI/CD to automatically validate prompt quality whenever prompts or code are updated.

---

# Features

- 100+ Golden Dataset Test Cases
- Prompt Evaluation using Promptfoo
- Google Gemini 3.1 Flash Lite Integration
- Automated GitHub Actions CI/CD
- Hallucination Detection
- Answer Quality Evaluation
- Pass/Fail Analysis
- Latency Monitoring
- P50 and P95 Latency Metrics
- Metrics History Tracking
- Interactive Streamlit Dashboard
- Automated Threshold Validation
- Multi-page Streamlit Web Application

---

# Project Structure

```text
llm-eval-pipeline/
│
├── .github/
│   └── workflows/
│       └── llm-eval.yml
│
├── .streamlit/
│   └── config.toml
│
├── dashboard/
│   └── app.py
│
├── datasets/
│   └── golden_dataset.csv
│
├── history/
│   └── metrics_history.csv
│
├── images/
│
├── pages/
│   ├── Golden_Dataset.py
│   ├── Run_Evaluation.py
│   ├── Dashboard.py
│   ├── Metrics_History.py
│   └── Project_Info.py
│
├── prompts/
│
├── scripts/
│   ├── check_results.py
│   └── save_metrics.py
│
├── Home.py
├── promptfooconfig.yaml
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/anuhya-7842/llm-eval-pipeline.git
```

Move into the project

```bash
cd llm-eval-pipeline
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the required Python packages

```bash
pip install -r requirements.txt
```

Install Promptfoo

```bash
npm install -g promptfoo
```

---

# Running the Evaluation

Run Promptfoo evaluation

```bash
promptfoo eval --output results.json
```

---

# Saving Evaluation Metrics

```bash
python scripts/save_metrics.py
```

---

# Checking Evaluation Thresholds

```bash
python scripts/check_results.py
```

---

# Running the Streamlit Application

```bash
https://anuhya-llm-promptfoo-configuration.streamlit.app/
```

---

# Dashboard Features

The dashboard displays the following evaluation metrics:

- Total Tests
- Passed Tests
- Failed Tests
- Pass Rate
- Hallucination Rate
- Average Latency
- P50 Latency
- P95 Latency
- Estimated Evaluation Cost
- Metrics History
- Evaluation Trends
- Historical Performance Charts

---

# Streamlit Pages

The application contains the following pages:

- Home
- Golden Dataset
- Run Evaluation
- Dashboard
- Metrics History
- Project Information

---

# GitHub Actions CI/CD Workflow

Every push to the **main** branch automatically performs the following tasks:

- Runs Promptfoo evaluation
- Executes all golden dataset test cases
- Calculates evaluation metrics
- Validates hallucination threshold
- Validates latency threshold
- Fails the pipeline if thresholds are exceeded
- Saves evaluation metrics

---

# Evaluation Metrics

The pipeline measures:

- Hallucination Rate
- Answer Relevancy
- Pass Rate
- Failed Tests
- Average Latency
- P50 Latency
- P95 Latency
- Estimated Evaluation Cost

---

# Technologies Used

- Python
- Streamlit
- Promptfoo
- Google Gemini 3.1 Flash Lite
- GitHub Actions
- Pandas
- CSV

---

# Project Objective

The objective of this project is to build a production-ready LLM Evaluation CI/CD Pipeline that continuously validates AI-generated responses, monitors performance, detects hallucinations, and provides historical evaluation insights through an interactive Streamlit dashboard.

---

# Project Demonstration

This project includes:

- Multi-page Streamlit Application
- Interactive Evaluation Dashboard
- Automated Prompt Evaluation Pipeline
- GitHub Actions CI/CD Workflow
- Historical Metrics Tracking
- Automated Threshold Validation
