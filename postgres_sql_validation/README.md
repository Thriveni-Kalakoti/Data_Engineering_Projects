# PostgreSQL-Style SQL Validation Pipeline

This project demonstrates a beginner-friendly Data Engineering validation workflow that loads sales data into a local database and runs SQL-based data quality checks.

The goal is to practice a common real-world Data Engineering task:

```text
CSV Data → Database Table → SQL Validation Checks → Python Validation Runner → Tests → CI
```

---

## Project Overview

This project performs the following steps:

1. Loads sales data from a CSV file.
2. Stores the data in a SQLite database table.
3. Runs SQL validation checks for row counts, nulls, duplicates, and invalid values.
4. Automates validation using Python.
5. Tests the load and validation logic using Pytest.
6. Runs automated checks using GitHub Actions.

---

## Business Scenario

In real data engineering workflows, loading data into a database or warehouse is not enough.

After data is loaded, Data Engineers must validate that:

- the expected number of rows loaded
- required fields are not null
- business keys are not duplicated
- numeric values are valid
- the table is ready for reporting, analytics, or downstream pipelines

This project simulates those checks using a small sales dataset and SQL validation logic.

---

## Architecture

```text
Sales CSV File
      ↓
Python Pandas Loader
      ↓
SQLite Database Table
      ↓
SQL Validation Checks
      ↓
Python Validation Runner
      ↓
Pytest + GitHub Actions CI
```

---

## Project Structure

```text
postgres_sql_validation/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
│   └── sales_data.csv
├── output/
│   └── sales_validation.db
├── sql/
│   └── validation_checks.sql
├── src/
│   ├── __init__.py
│   ├── load_sales.py
│   └── validate_sales.py
└── tests/
    ├── __init__.py
    └── test_validation.py
```

---

## Folder Explanation

- `data/sales_data.csv` → Sample sales input data.
- `sql/validation_checks.sql` → SQL validation queries.
- `src/load_sales.py` → Loads CSV data into a SQLite database table.
- `src/validate_sales.py` → Runs validation checks and prints pass/fail results.
- `tests/test_validation.py` → Tests data loading and validation logic.
- `output/` → Stores generated database output.
- `requirements.txt` → Lists Python dependencies.
- `.gitignore` → Prevents generated files and local environment files from being committed.

---

## Tools & Technologies

- **Python** – Main programming language
- **Pandas** – CSV loading and DataFrame handling
- **SQLite** – Local database used for validation practice
- **SQL** – Data quality validation checks
- **Pytest** – Unit testing
- **GitHub Actions** – CI workflow
- **Git/GitHub** – Version control and pull request workflow

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Thriveni-Kalakoti/Data_Engineering_Projects.git
cd Data_Engineering_Projects/postgres_sql_validation
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

## Run the Data Load

From inside the `postgres_sql_validation` folder, run:

```bash
python src/load_sales.py
```

Expected output:

```text
Rows loaded into database: 5
```

---

## Run SQL Validation Manually

Open SQLite:

```bash
sqlite3 output/sales_validation.db
```

Inside SQLite, run:

```sql
.read sql/validation_checks.sql
.exit
```

Expected output:

```text
5
0
0
0
0
```

Meaning:

| Output | Check |
|---|---|
| `5` | Total row count |
| `0` | Null key count |
| `0` | Duplicate order ID count |
| `0` | Negative sales count |
| `0` | Invalid quantity count |

---

## Run Python Validation

From inside the `postgres_sql_validation` folder, run:

```bash
python src/validate_sales.py
```

Expected output:

```text
Validation Results:
total_rows: 5
null_key_count: 0
duplicate_order_id_count: 0
negative_sales_count: 0
invalid_quantity_count: 0
All validation checks passed.
```

---

## Run Tests

From inside the `postgres_sql_validation` folder, run:

```bash
pytest tests
```

Expected output:

```text
4 passed
```

---

## Validation Checks Implemented

| Validation Check | Purpose |
|---|---|
| Row count check | Confirms data was loaded |
| Null key check | Ensures required fields are present |
| Duplicate order ID check | Detects duplicate business keys |
| Negative sales check | Detects invalid sales values |
| Invalid quantity check | Detects zero or negative quantity values |

---

## CI/CD

GitHub Actions runs automated checks when code is pushed.

The CI workflow validates:

- Python dependencies install correctly
- Python files compile successfully
- Pytest tests pass

The workflow file is stored at the repository root:

```text
.github/workflows/ci.yml
```

---

## Why This Project Matters

This project demonstrates a key Data Engineering responsibility: validating loaded data before it is used by reporting, analytics, machine learning, or AI workflows.

In real companies, these checks help prevent bad data from reaching dashboards, stakeholders, and downstream systems.

---

## Future Improvements

- Upgrade SQLite workflow to PostgreSQL
- Add Great Expectations for data quality checks
- Add structured logging
- Add failure handling and alerts
- Add Docker support
- Add Airflow orchestration
- Add cloud warehouse validation using BigQuery, Snowflake, or Redshift