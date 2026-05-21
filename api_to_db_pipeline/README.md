# API to Database Pipeline

This project demonstrates a beginner-friendly Data Engineering pipeline that extracts data from a public REST API, transforms the JSON response into a structured tabular format, and loads the cleaned data into a local SQLite database.

The goal is to practice a common real-world data engineering workflow:

```text
REST API → JSON → Python → Pandas → SQLite Database → Validation → Tests → CI
```

---

## Project Overview

This pipeline performs the following steps:

1. **Extract** data from a public REST API.
2. **Transform** nested JSON records into a clean tabular DataFrame.
3. **Load** the transformed data into a SQLite database.
4. **Validate** the database load using row-count checks.
5. **Test** transformation and load logic using Pytest.
6. **Run CI checks** using GitHub Actions.

---

## Business Scenario

Many organizations collect operational data from external or internal APIs such as ServiceNow, Jira, Salesforce, Workday, monitoring tools, cloud services, and internal platforms.

A Data Engineer is often responsible for building pipelines that pull this API data, clean it, convert it into structured tables, load it into a database or warehouse, and validate that the load completed correctly.

This project simulates that workflow using a public API and a local SQLite database.

---

## Architecture

```text
Public REST API
      ↓
Python requests
      ↓
Raw JSON response
      ↓
Pandas json_normalize
      ↓
Clean structured DataFrame
      ↓
SQLite database table
      ↓
Row-count validation
      ↓
Pytest + GitHub Actions
```

---

## Data Source

This project uses the public JSONPlaceholder users API:

```text
https://jsonplaceholder.typicode.com/users
```

The API returns sample user records in JSON format, including nested fields such as address and company information.

---

## Project Structure

```text
api_to_db_pipeline/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
├── output/
│   └── api_users.db
├── src/
│   ├── __init__.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── pipeline.py
└── tests/
    ├── __init__.py
    └── test_pipeline.py
```

---

## Folder Explanation

- `src/extract.py` → Extracts JSON data from the public REST API.
- `src/transform.py` → Flattens nested JSON and converts it into a clean DataFrame.
- `src/load.py` → Loads the transformed DataFrame into SQLite and validates row count.
- `src/pipeline.py` → Runs the full pipeline from extraction to validation.
- `tests/test_pipeline.py` → Tests transformation and database load logic.
- `output/` → Stores generated SQLite database output.
- `requirements.txt` → Lists Python dependencies.
- `.gitignore` → Prevents generated files, cache files, and local environment files from being committed.

---

## Tools & Technologies

- **Python** – Main programming language
- **requests** – API extraction
- **Pandas** – JSON normalization and data transformation
- **SQLite** – Local relational database
- **Pytest** – Unit testing
- **GitHub Actions** – CI workflow
- **Git/GitHub** – Version control and pull request workflow

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Thriveni-Kalakoti/Data_Engineering_Projects.git
cd Data_Engineering_Projects/api_to_db_pipeline
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

## Run the Full Pipeline

From inside the `api_to_db_pipeline` folder, run:

```bash
python src/pipeline.py
```

Expected output:

```text
Starting API to database pipeline...
Records extracted: 10
Rows transformed: 10
Data loaded into SQLite database.
Rows validated in database: 10
Pipeline completed successfully.
```

---

## Run Individual Steps

### Extract API data

```bash
python src/extract.py
```

### Transform API records

```bash
python src/transform.py
```

---

## Run Tests

From inside the `api_to_db_pipeline` folder, run:

```bash
pytest tests
```

Expected output:

```text
3 passed
```

---

## Data Transformations Performed

The pipeline transforms nested API JSON into a flat database-ready structure.

Selected fields:

| Raw Field | Transformed Column |
|---|---|
| `id` | `user_id` |
| `name` | `name` |
| `username` | `username` |
| `email` | `email` |
| `address.city` | `city` |
| `address.zipcode` | `zipcode` |
| `company.name` | `company_name` |

---

## Validation Logic

The pipeline validates the load by comparing:

```text
Number of transformed rows = Number of rows loaded into SQLite table
```

If the row counts do not match, the pipeline raises an error.

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

This project demonstrates a common Data Engineering workflow used in real business systems:

```text
API ingestion → JSON parsing → transformation → database load → validation → testing → CI
```

It builds practical experience with API-based ingestion, which is used heavily in enterprise data pipelines.

---

## Future Improvements

- Load data into PostgreSQL instead of SQLite
- Add API pagination handling
- Add retry logic for failed API calls
- Add structured logging
- Add data quality checks
- Add Docker support
- Schedule the pipeline using Airflow
- Load data into a cloud warehouse such as BigQuery or Snowflake