import sqlite3
from pathlib import Path

import pandas as pd


DATA_PATH = "data/sales_data.csv"
DB_PATH = "output/sales_validation.db"
TABLE_NAME = "sales"


def load_sales_data(
    data_path: str = DATA_PATH,
    db_path: str = DB_PATH,
    table_name: str = TABLE_NAME
) -> int:
    """
    Load sales CSV data into a SQLite database table.

    Args:
        data_path: Path to the input CSV file.
        db_path: Path to the output SQLite database.
        table_name: Target database table name.

    Returns:
        Number of rows loaded.
    """
    df = pd.read_csv(data_path)

    required_columns = [
        "order_id",
        "order_date",
        "customer_id",
        "product_category",
        "sales",
        "quantity",
        "region"
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)

    return len(df)


if __name__ == "__main__":
    row_count = load_sales_data()
    print(f"Rows loaded into database: {row_count}")