# CSV to SQLite ETL Pipeline

This beginner-level data engineering project demonstrates a simple ETL pipeline that reads a raw CSV file, cleans it using Python and Pandas, and loads it into an SQLite database.

---

## Project Objectives

- **Extract:** Read raw sales data from `superstore.csv`
- **Transform:** Clean the data (drop nulls, rename columns, convert dates)
- **Load:** Insert clean data into a SQLite table

---

##  Tools & Libraries Used

- **Python 3.8+**
- **Pandas** for data manipulation
- **SQLite3** for lightweight relational database

---

##  Key Concepts Practiced

- File handling and CSV ingestion
- Data cleaning and transformation
- Writing data to relational databases
- Basic ETL pipeline logic (Extract → Transform → Load)

---

##  Data Source

Dataset: [Superstore Sales Dataset on Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

---

##  How to Run

1. Download the CSV file and place it in this folder as `superstore.csv`
2. Run the Python script:
   ```bash
   python etl_script.py
3. A new file named superstore.db will be created. You can query it using any SQLite viewer or browser plugin.
