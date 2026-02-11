# CSV to SQLite ETL Pipeline

This project demonstrates a simple, modular ETL (Extract → Transform → Load) pipeline built using Python and SQLite. 

The pipeline reads raw sales data from a CSV file, performs basic data validation and cleaning, and loads the cleaned dataset into a SQLite database.

This project follows a clean, minimal repository structure similar to how small internal data engineering tasks are structured in real-world environments.

---

## Project Overview

The goal of this project is to simulate a basic data engineering workflow:

- **Extract:** Read raw sales data from a CSV file
- **Transform:** Validate required columns, clean null values, convert dates, standardize column names
- **Load:** Insert cleaned data into a SQLite database table

---

## Project Structure

```
.
├── .github
│   └── workflows
│       └── ci.yml
├── .gitignore
├── data
│   └── superstore.csv
├── output
│   └── superstore.db
├── README.md
├── requirements.txt
├── src
│   ├── db.py
│   └── etl.py
└── tests
```

### Folder Explanation

- `data/` → Contains raw input dataset  
- `src/` → Contains ETL pipeline source code  
- `output/` → Contains generated SQLite database (not tracked in git)  
- `.github/workflows/` → Basic CI configuration  

---

## Tools & Libraries Used

- **Python 3.9+**
- **Pandas** – Data manipulation and cleaning
- **SQLite3** – Lightweight relational database (built into Python)
- **GitHub Actions** – Basic CI workflow

---

## Data Source

Dataset used:
Superstore Sales Dataset (Kaggle)

https://www.kaggle.com/datasets/vivek468/superstore-dataset-final

The dataset should be placed at:

```
data/superstore.csv
```

---

## Setup Instructions (Mac / Linux)

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd csv-to-sqlite-etl
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

## Run the ETL Pipeline

```bash
python src/etl.py
```

You should see logs similar to:

```
Reading: data/superstore.csv
Rows extracted: XXXX
Rows after transform: XXXX
Loaded into: output/superstore.db
```

After successful execution, a new database file will be created at:

```
output/superstore.db
```

---

## Verifying the Output

### Option 1 – Using Mac Terminal

Run:

```bash
sqlite3 output/superstore.db
```

Inside sqlite:

```sql
.tables
SELECT COUNT(*) FROM sales;
SELECT * FROM sales LIMIT 5;
.exit
```

### Option 2 – Using VS Code SQLite Extension

1. Install "SQLite" extension in VS Code
2. Right-click `output/superstore.db`
3. Open Database
4. Run SQL queries

---

## Data Transformations Performed

- Validates required columns exist
- Drops rows with null values in required fields
- Converts date columns to datetime format
- Removes invalid date rows
- Standardizes column names:
  - Lowercase
  - Replace spaces with underscores
  - Remove special characters

---

## Example Query

```sql
SELECT SUM(sales) AS total_sales FROM sales;
```

---

## Why This Project Matters

This project demonstrates:

- Basic data engineering workflow
- Clean project structure
- Modular code design
- Simple validation logic
- Writing data into relational databases
- Basic CI integration

It serves as a foundational ETL pipeline before moving into more advanced tools such as PostgreSQL, Airflow, Docker, and cloud storage systems.

