# API to Database Pipeline

This project demonstrates a beginner-friendly Data Engineering pipeline that extracts data from a public REST API, transforms the JSON response into a structured format, and loads the cleaned data into a local database.

The goal is to practice a common real-world data engineering workflow:

```text
API → JSON → Python → Pandas → Database → Validation
```

---

## Project Goal

The goal of this project is to build a simple API ingestion pipeline that:

- Calls a public REST API
- Extracts JSON data
- Converts JSON into a structured table
- Cleans and standardizes the data
- Loads the result into a database
- Validates the pipeline output
- Uses tests and CI/CD for basic quality checks

---

## Why This Project Matters

Many Data Engineering pipelines start by collecting data from external systems through APIs.

In real companies, APIs are commonly used to ingest data from:

- SaaS applications
- internal services
- finance systems
- HR systems
- marketing platforms
- monitoring tools
- cloud services
- AI/ML platforms

This project helps build the foundation for API-based ingestion workflows.

---

## Planned Architecture

```text
Public REST API
      ↓
Python requests
      ↓
Raw JSON response
      ↓
Pandas transformation
      ↓
SQLite database
      ↓
Validation checks
      ↓
Pytest + GitHub Actions CI
```

---

## Project Structure

```text
api_to_db_pipeline/
├── README.md
├── requirements.txt
├── .gitignore
├── data/
├── output/
├── src/
│   └── __init__.py
└── tests/
    └── __init__.py
```

---

## Tools & Technologies

- **Python** – main programming language
- **requests** – used to call REST APIs
- **Pandas** – used for data transformation
- **SQLite** – local database for storing transformed data
- **Pytest** – testing framework
- **GitHub Actions** – CI workflow for automated validation
- **Git/GitHub** – version control and portfolio publishing

---

## Current Status

This project is currently in setup stage.

Completed:

- Created project folder structure
- Added starter files
- Added requirements file
- Added `.gitignore`

Next steps:

- Add API extraction logic
- Add transformation logic
- Add database loading logic
- Add tests
- Add CI validation