import sys
from pathlib import Path

import pandas as pd
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.etl import transform


def test_import_etl_module():
    import src.etl
    assert src.etl is not None


def test_import_db_module():
    import src.db
    assert src.db is not None


def test_transform_standardizes_columns_and_converts_dates():
    sample_data = pd.DataFrame({
        "Order ID": ["CA-001", "CA-002"],
        "Order Date": ["2024-01-01", "2024-01-02"],
        "Ship Date": ["2024-01-03", "2024-01-04"],
        "Customer ID": ["C001", "C002"],
        "Sales": [100.50, 250.75],
        "Quantity": [2, 5],
        "Profit": [20.00, 45.50]
    })

    transformed_df = transform(sample_data)

    assert "order_id" in transformed_df.columns
    assert "order_date" in transformed_df.columns
    assert "ship_date" in transformed_df.columns
    assert "customer_id" in transformed_df.columns

    assert pd.api.types.is_datetime64_any_dtype(transformed_df["order_date"])
    assert pd.api.types.is_datetime64_any_dtype(transformed_df["ship_date"])

    assert len(transformed_df) == 2


def test_transform_drops_rows_with_missing_required_values():
    sample_data = pd.DataFrame({
        "Order ID": ["CA-001", None],
        "Order Date": ["2024-01-01", "2024-01-02"],
        "Ship Date": ["2024-01-03", "2024-01-04"],
        "Customer ID": ["C001", "C002"],
        "Sales": [100.50, 250.75],
        "Quantity": [2, 5],
        "Profit": [20.00, 45.50]
    })

    transformed_df = transform(sample_data)

    assert len(transformed_df) == 1
    assert transformed_df.iloc[0]["order_id"] == "CA-001"


def test_transform_raises_error_when_required_column_missing():
    sample_data = pd.DataFrame({
        "Order ID": ["CA-001"],
        "Order Date": ["2024-01-01"],
        "Ship Date": ["2024-01-03"],
        "Customer ID": ["C001"],
        "Sales": [100.50],
        "Quantity": [2]
    })

    with pytest.raises(ValueError, match="Missing required columns"):
        transform(sample_data)
