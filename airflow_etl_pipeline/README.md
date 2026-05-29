# Airflow ETL Pipeline

This project demonstrates a Data Engineering workflow orchestrated with Apache Airflow.

The goal is to practice a common production-style pattern:

```text
CSV Data → ETL Python Tasks → Airflow DAG → Task Dependencies → Tests → CI
```

---

## Project Overview

This project performs the following steps:

1. Reads customer order data from a CSV file.
2. Cleans and validates required fields.
3. Removes rows with missing or invalid values.
4. Saves processed data to an output CSV file.
5. Defines an Airflow DAG to orchestrate the ETL task.
6. Validates ETL logic and DAG imports using Pytest.
7. Runs automated checks using GitHub Actions.

---

## Business Scenario

In real Data Engineering teams, pipelines are not usually run manually. They are scheduled, monitored, retried, and logged using orchestration tools.

Apache Airflow is commonly used to define pipeline workflows as DAGs, schedule recurring jobs, manage task dependencies, retry failed tasks, and monitor pipeline execution.

This project simulates that workflow using a customer orders ETL pipeline.

---

## Architecture

```text
Customer Orders CSV
      ↓
Extract Task Logic
      ↓
Transform Task Logic
      ↓
Load Task Logic
      ↓
Airflow DAG
      ↓
Pytest + GitHub Actions CI
```

---

## Project Structure

```text
airflow_etl_pipeline/
├── README.md
├── requirements.txt
├── .gitignore
├── dags/
│   └── customer_orders_dag.py
├── data/
│   └── customer_orders.csv
├── output/
│   └── processed_customer_orders.csv
├── src/
│   ├── __init__.py
│   └── etl_tasks.py
└── tests/
    ├── __init__.py
    ├── test_dag_import.py
    └── test_etl_tasks.py
```

---

## Tools & Technologies

- **Python** – ETL task logic
- **Pandas** – Data cleaning and transformation
- **Apache Airflow** – Workflow orchestration
- **Pytest** – Unit testing and DAG import validation
- **GitHub Actions** – CI workflow
- **Git/GitHub** – Version control and pull request workflow

---

## Run ETL Logic Locally

From inside the `airflow_etl_pipeline` folder, run:

```bash
python src/etl_tasks.py
```

Expected output:

```text
Starting Airflow ETL pipeline task logic...
Rows extracted: 5
Rows after transformation: 4
Processed data saved to: output/processed_customer_orders.csv
ETL task logic completed successfully.
```

---

## Validate Airflow DAG Import

```bash
python dags/customer_orders_dag.py
```

Expected result:

```text
No output means the DAG imported successfully.
```

---

## Run Tests

```bash
pytest tests
```

Expected output:

```text
6 passed
```

---

## Airflow DAG Details

DAG ID:

```text
customer_orders_etl_pipeline
```

Task flow:

```text
start → run_customer_orders_etl → end
```

DAG features:

- Daily schedule
- Retry configuration
- Task dependency definition
- PythonOperator-based ETL execution
- DAG import validation through tests

---

## Data Transformations Performed

The ETL logic:

- Validates required columns
- Removes rows with missing required values
- Converts `order_date` to datetime format
- Removes invalid dates
- Removes zero or negative order amounts
- Saves processed customer order data to CSV

---

## CI/CD

GitHub Actions validates this project automatically.

The CI workflow checks:

- Python dependencies install correctly
- Python files compile successfully
- Airflow DAG imports successfully through tests
- ETL unit tests pass

The workflow file is stored at the repository root:

```text
.github/workflows/ci.yml
```

---

## Why This Project Matters

This project demonstrates workflow orchestration, which is a core Data Engineering skill.

It shows how ETL logic can be organized into reusable Python functions and connected to an Airflow DAG for scheduled, monitored, and retryable execution.

---

## Future Improvements

- Run Airflow locally with Docker Compose
- Add separate extract, transform, and load Airflow tasks
- Add database load step
- Add data quality validation task
- Add failure alerting
- Add cloud storage integration
- Deploy DAG to a managed Airflow environment such as Cloud Composer, MWAA, or Astronomer