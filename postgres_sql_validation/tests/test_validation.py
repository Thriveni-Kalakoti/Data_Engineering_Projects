import sys
from pathlib import Path

import pandas as pd
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.load_sales import load_sales_data
from src.validate_sales import run_validation_checks, validate_results


def test_load_sales_data_loads_rows(tmp_path):
    test_csv = tmp_path / "sales_data.csv"
    test_db = tmp_path / "sales_validation.db"

    sample_df = pd.DataFrame({
        "order_id": ["ORD-001", "ORD-002"],
        "order_date": ["2024-01-01", "2024-01-02"],
        "customer_id": ["CUST-001", "CUST-002"],
        "product_category": ["Technology", "Furniture"],
        "sales": [1200.50, 450.00],
        "quantity": [2, 1],
        "region": ["East", "West"]
    })

    sample_df.to_csv(test_csv, index=False)

    row_count = load_sales_data(
        data_path=str(test_csv),
        db_path=str(test_db),
        table_name="sales"
    )

    assert row_count == 2


def test_validation_checks_pass_for_clean_data(tmp_path):
    test_csv = tmp_path / "sales_data.csv"
    test_db = tmp_path / "sales_validation.db"

    sample_df = pd.DataFrame({
        "order_id": ["ORD-001", "ORD-002"],
        "order_date": ["2024-01-01", "2024-01-02"],
        "customer_id": ["CUST-001", "CUST-002"],
        "product_category": ["Technology", "Furniture"],
        "sales": [1200.50, 450.00],
        "quantity": [2, 1],
        "region": ["East", "West"]
    })

    sample_df.to_csv(test_csv, index=False)

    load_sales_data(
        data_path=str(test_csv),
        db_path=str(test_db),
        table_name="sales"
    )

    checks = run_validation_checks(db_path=str(test_db), table_name="sales")

    assert checks["total_rows"] == 2
    assert checks["null_key_count"] == 0
    assert checks["duplicate_order_id_count"] == 0
    assert checks["negative_sales_count"] == 0
    assert checks["invalid_quantity_count"] == 0
    assert validate_results(checks) is True


def test_validate_results_fails_for_bad_data():
    checks = {
        "total_rows": 2,
        "null_key_count": 1,
        "duplicate_order_id_count": 0,
        "negative_sales_count": 0,
        "invalid_quantity_count": 0
    }

    assert validate_results(checks) is False


def test_load_sales_data_raises_error_for_missing_columns(tmp_path):
    test_csv = tmp_path / "bad_sales_data.csv"
    test_db = tmp_path / "sales_validation.db"

    bad_df = pd.DataFrame({
        "order_id": ["ORD-001"],
        "sales": [100.00]
    })

    bad_df.to_csv(test_csv, index=False)

    with pytest.raises(ValueError, match="Missing required columns"):
        load_sales_data(
            data_path=str(test_csv),
            db_path=str(test_db),
            table_name="sales"
        )