import sqlite3


DB_PATH = "output/sales_validation.db"
TABLE_NAME = "sales"


def run_validation_checks(
    db_path: str = DB_PATH,
    table_name: str = TABLE_NAME
) -> dict:
    """
    Run SQL data quality validation checks against the sales table.

    Args:
        db_path: SQLite database file path.
        table_name: Target table name.

    Returns:
        Dictionary containing validation check results.
    """
    checks = {}

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()

        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        checks["total_rows"] = cursor.fetchone()[0]

        cursor.execute(
            f"""
            SELECT COUNT(*)
            FROM {table_name}
            WHERE order_id IS NULL
               OR order_date IS NULL
               OR customer_id IS NULL
            """
        )
        checks["null_key_count"] = cursor.fetchone()[0]

        cursor.execute(
            f"""
            SELECT COUNT(*)
            FROM (
                SELECT order_id
                FROM {table_name}
                GROUP BY order_id
                HAVING COUNT(*) > 1
            )
            """
        )
        checks["duplicate_order_id_count"] = cursor.fetchone()[0]

        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE sales < 0")
        checks["negative_sales_count"] = cursor.fetchone()[0]

        cursor.execute(f"SELECT COUNT(*) FROM {table_name} WHERE quantity <= 0")
        checks["invalid_quantity_count"] = cursor.fetchone()[0]

    return checks


def validate_results(checks: dict) -> bool:
    """
    Validate SQL check results against expected data quality rules.

    Args:
        checks: Dictionary of validation check results.

    Returns:
        True if all checks pass.
    """
    if checks["total_rows"] <= 0:
        return False

    if checks["null_key_count"] != 0:
        return False

    if checks["duplicate_order_id_count"] != 0:
        return False

    if checks["negative_sales_count"] != 0:
        return False

    if checks["invalid_quantity_count"] != 0:
        return False

    return True


if __name__ == "__main__":
    validation_results = run_validation_checks()

    print("Validation Results:")
    for check_name, check_value in validation_results.items():
        print(f"{check_name}: {check_value}")

    if validate_results(validation_results):
        print("All validation checks passed.")
    else:
        raise ValueError("One or more validation checks failed.")