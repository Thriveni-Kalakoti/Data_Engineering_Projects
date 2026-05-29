# Dockerized Data Pipeline

This project demonstrates a beginner-friendly Data Engineering pipeline that runs both locally and inside a Docker container.

The goal is to practice a common real-world engineering workflow:

```text
CSV Data → Python ETL → Cleaned Output → Docker Container → Tests → CI
```

---

## Project Overview

This pipeline performs the following steps:

1. Reads raw order data from a CSV file.
2. Cleans and validates required fields.
3. Removes rows with missing or invalid values.
4. Saves the cleaned output as a CSV file.
5. Runs locally using Python.
6. Runs inside a Docker container.
7. Validates logic using Pytest.
8. Runs automated checks using GitHub Actions.

---

## Business Scenario

In real companies, data pipelines should not depend only on one developer’s laptop setup.

A pipeline may work locally but fail in CI, a server, or a cloud environment because of different Python versions, missing packages, or environment differences.

Docker helps package the code, dependencies, and run command into a container so the pipeline can run consistently across environments.

---

## Architecture

```text
Raw Orders CSV
      ↓
Python ETL Pipeline
      ↓
Cleaned Orders CSV
      ↓
Docker Image
      ↓
Docker Container Run
      ↓
Pytest + GitHub Actions CI
```

---

## Project Structure

```text
dockerized_data_pipeline/
├── README.md
├── requirements.txt
├── .gitignore
├── Dockerfile
├── data/
│   └── orders.csv
├── output/
│   └── cleaned_orders.csv
├── src/
│   ├── __init__.py
│   └── pipeline.py
└── tests/
    ├── __init__.py
    └── test_pipeline.py
```

---

## Tools & Technologies

- **Python** – Main programming language
- **Pandas** – Data cleaning and transformation
- **Docker** – Containerized pipeline execution
- **Pytest** – Unit testing
- **GitHub Actions** – CI workflow
- **Git/GitHub** – Version control and pull request workflow

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Thriveni-Kalakoti/Data_Engineering_Projects.git
cd Data_Engineering_Projects/dockerized_data_pipeline
```

### 2. Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run Pipeline Locally

From inside the `dockerized_data_pipeline` folder, run:

```bash
python src/pipeline.py
```

Expected output:

```text
Starting dockerized data pipeline...
Rows extracted: 5
Rows after transformation: 4
Cleaned data saved to: output/cleaned_orders.csv
Pipeline completed successfully.
```

---

## Run Tests Locally

```bash
pytest tests
```

Expected output:

```text
4 passed
```

---

## Build Docker Image

From inside the `dockerized_data_pipeline` folder, run:

```bash
docker build -t dockerized-data-pipeline .
```

---

## Run Docker Container

```bash
docker run --rm dockerized-data-pipeline
```

Expected output:

```text
Starting dockerized data pipeline...
Rows extracted: 5
Rows after transformation: 4
Cleaned data saved to: output/cleaned_orders.csv
Pipeline completed successfully.
```

---

## Data Transformations Performed

The pipeline performs these data cleaning steps:

- Validates required columns exist
- Removes rows with missing required values
- Converts `order_date` into datetime format
- Removes invalid dates
- Removes rows where `amount` is zero or negative
- Saves cleaned data to `output/cleaned_orders.csv`

---

## Why Docker Matters

Docker makes the pipeline reproducible.

Without Docker, a pipeline may depend on a developer’s local Python version, installed packages, or machine setup.

With Docker, the pipeline runs inside a clean container that includes:

- Python runtime
- required dependencies
- pipeline code
- input data
- execution command

This makes the project easier to run in CI/CD, servers, cloud environments, and production-style workflows.

---

## CI/CD

GitHub Actions validates this project automatically.

The CI workflow checks:

- Python dependencies install correctly
- Python files compile successfully
- Pytest tests pass
- Docker image builds successfully
- Docker container runs successfully

The workflow file is stored at the repository root:

```text
.github/workflows/ci.yml
```

---

## Interview Summary

This project shows how to containerize a data pipeline using Docker so it can run consistently across environments.

It demonstrates practical Data Engineering skills such as ETL development, data cleaning, automated testing, Docker image creation, container execution, and CI validation through GitHub Actions.

---

## Future Improvements

- Add PostgreSQL as a target database
- Add structured logging
- Add environment-based configuration
- Add Docker Compose
- Add Airflow orchestration
- Push Docker image to Docker Hub or GitHub Container Registry
- Deploy as a scheduled cloud job