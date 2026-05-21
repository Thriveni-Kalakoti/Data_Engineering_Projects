import sqlite3
from pathlib import Path

import pandas as pd


DEFAULT_DB_PATH = "output/api_users.db"


def load_to_sqlite(
    df: pd.DataFrame,
    db_path: str = DEFAULT_DB_PATH,
    table_name: str = "users"
) -> None:
    """
    Load a transformed DataFrame into a SQLite database table.

    Args:
        df: Clean DataFrame ready for loading.
        db_path: SQLite database file path.
        table_name: Target table name.
    """
    if df.empty:
        raise ValueError("Cannot load an empty DataFrame.")

    Path(db_path).parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(db_path) as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)


def validate_load(
    db_path: str = DEFAULT_DB_PATH,
    table_name: str = "users"
) -> int:
    """
    Validate database load by counting rows in the target table.

    Args:
        db_path: SQLite database file path.
        table_name: Target table name.

    Returns:
        Row count from the database table.
    """
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = cursor.fetchone()[0]

    return row_count