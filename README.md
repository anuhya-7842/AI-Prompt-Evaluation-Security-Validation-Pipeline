# LLM Evaluation CI/CD Pipeline

## Overview

This project implements an automated evaluation pipeline for Large Language Models (LLMs) using Promptfoo, GitHub Actions, and Streamlit.

The pipeline automatically evaluates prompt quality whenever code or prompts are updated, similar to unit testing in software development.

---

## Features

- 100+ Golden Dataset Test Cases
- Prompt Evaluation using Promptfoo
- Google Gemini 3.1 Flash Lite
- Automated GitHub Actions CI/CD
- Hallucination Detection
- Latency Measurement
- P50 & P95 Latency
- Streamlit Dashboard
- Evaluation Threshold Checking
- Metrics History Tracking

---

## Project Structure

```
llm-eval-pipeline/
│
├── .github/
│   └── workflows/
│       └── llm-eval.yml
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
├── prompts/
│   └── rag_system_prompt.txt
│
├── scripts/
│   ├── check_results.py
│   └── save_metrics.py
│
├── promptfooconfig.yaml
├── results.json
├── README.md
└── .gitignore
```

---

## Installation

```bash
git clone https://github.com/anuhya-7842/llm-eval-pipeline.git

cd llm-eval-pipeline

python -m venv venv

venv\Scripts\activate

pip install streamlit

npm install -g promptfoo
```

---

## Environment Variable

Create a `.env` file.

```
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## Run Evaluation

```
npx promptfoo eval --env-file .env
```

---

## Run Dashboard

```
cd dashboard

streamlit run app.py
```

---

## Threshold Check

```
python scripts/check_results.py
```

---

## Save Evaluation History

```
python scripts/save_metrics.py
```

---

## Dashboard Metrics

- Total Tests
- Passed Tests
- Failed Tests
- Hallucination Rate
- Pass Rate
- Average Latency
- P50 Latency
- P95 Latency
- Estimated Cost
- Metrics History

---

## CI/CD

Every push automatically:

- Runs Promptfoo evaluation
- Checks evaluation thresholds
- Blocks failing evaluations
- Saves evaluation metrics

---

## Technologies

- Python
- Promptfoo
- Streamlit
- GitHub Actions
- Google Gemini 3.1 Flash Lite