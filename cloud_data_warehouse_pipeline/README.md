# Cloud Data Warehouse Pipeline

This project demonstrates a cloud data warehouse preparation workflow for ecommerce order data.

The goal is to practice a common Data Engineering pattern:

```text
Raw CSV Data → Python Cleaning → Warehouse-Ready Dataset → BigQuery-Style SQL Queries → Tests → CI
```

---

## Project Overview

This project performs the following steps:

1. Reads raw ecommerce order data from a CSV file.
2. Cleans and validates required fields.
3. Removes rows with missing or invalid values.
4. Adds warehouse-friendly partition columns.
5. Saves cleaned data as a BigQuery-ready CSV file.
6. Includes BigQuery-style SQL validation and analytics queries.
7. Tests transformation and load logic using Pytest.
8. Runs automated checks using GitHub Actions.

---

## Business Scenario

In real companies, Data Engineers often prepare cleaned datasets for cloud data warehouses such as BigQuery, Snowflake, Redshift, Azure Synapse, or Databricks SQL.

Before data is loaded into a warehouse, it must be cleaned, validated, structured, and made ready for analytics, dashboards, machine learning, and AI use cases.

This project simulates that workflow using ecommerce orders data.

---

## Architecture

```text
Raw Ecommerce Orders CSV
      ↓
Python Cleaning Pipeline
      ↓
Warehouse-Ready CSV
      ↓
BigQuery-Style SQL Validation
      ↓
Analytics Queries
      ↓
Pytest + GitHub Actions CI
```

---

## Project Structure

```text
cloud_data_warehouse_pipeline/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── ecommerce_orders.csv
├── output/
│   └── ecommerce_orders_clean.csv
├── sql/
│   └── bigquery_validation_queries.sql
├── src/
│   ├── __init__.py
│   └── prepare_orders.py
└── tests/
    ├── __init__.py
    └── test_prepare_orders.py
```

---

## Tools & Technologies

- **Python** – Data preparation logic
- **Pandas** – Data cleaning and transformation
- **SQL** – Warehouse validation and analytics queries
- **BigQuery-style SQL** – Cloud warehouse query practice
- **Pytest** – Unit testing
- **GitHub Actions** – CI workflow
- **Git/GitHub** – Version control and pull request workflow

---

## Run Pipeline Locally

From inside the `cloud_data_warehouse_pipeline` folder, run:

```bash
python src/prepare_orders.py
```

Expected output:

```text
Starting cloud data warehouse preparation pipeline...
Rows extracted: 6
Rows after transformation: 4
Clean warehouse-ready data saved to: output/ecommerce_orders_clean.csv
Cloud warehouse preparation pipeline completed successfully.
```

---

## Run Tests

```bash
pytest tests
```

Expected output:

```text
4 passed
```

---

## Data Cleaning Rules

The pipeline performs the following cleaning steps:

- Validates required columns exist
- Removes rows with missing required fields
- Converts `order_date` into datetime format
- Removes invalid dates
- Removes zero or negative order amounts
- Removes zero or negative quantity values
- Adds `order_year` and `order_month` partition-style columns
- Saves cleaned output as a warehouse-ready CSV file

---

## BigQuery-Style SQL Queries

The SQL file includes:

```text
sql/bigquery_validation_queries.sql
```

Queries included:

- Row count validation
- Null key validation
- Duplicate order ID validation
- Invalid amount validation
- Revenue by product category
- Monthly revenue trend

These queries simulate checks and analytics commonly performed after loading data into a cloud data warehouse.

---

## Example Warehouse Table

Target table placeholder used in SQL:

```text
project_id.dataset_id.ecommerce_orders
```

In a real BigQuery project, this would be replaced with the actual:

```text
gcp_project.dataset.table_name
```

---

## CI/CD

GitHub Actions validates this project automatically.

The CI workflow checks:

- Python dependencies install correctly
- Python files compile successfully
- Pytest tests pass

The workflow file is stored at the repository root:

```text
.github/workflows/ci.yml
```

---

## Why This Project Matters

This project demonstrates how raw data can be prepared for cloud data warehouse loading and analytics.

It shows practical Data Engineering skills such as data cleaning, validation, partition-style column creation, SQL analytics, testing, and CI/CD.

---

## Future Improvements

- Load the cleaned CSV into Google BigQuery
- Add BigQuery Python client integration
- Add cloud storage staging step
- Add schema definition file
- Add data quality checks after warehouse load
- Add dbt models
- Add Airflow orchestration
- Add dashboard layer using Looker Studio or Power BI