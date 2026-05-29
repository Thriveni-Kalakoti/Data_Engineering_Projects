import sys
from pathlib import Path

import pandas as pd
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.prepare_orders import transform_orders, load_clean_orders


def test_transform_orders_removes_invalid_rows():
    sample_df = pd.DataFrame({
        "order_id": ["ORD-001", "ORD-002", "ORD-003"],
        "order_date": ["2024-01-01", "2024-01-02", "2024-01-03"],
        "customer_id": ["CUST-001", "CUST-002", "CUST-003"],
        "product_category": ["Electronics", "Furniture", "Office Supplies"],
        "order_amount": [1200.50, None, -25.00],
        "quantity": [1, 2, 1],
        "country": ["USA", "USA", "Canada"],
        "payment_status": ["paid", "paid", "failed"]
    })

    transformed_df = transform_orders(sample_df)

    assert len(transformed_df) == 1
    assert transformed_df.iloc[0]["order_id"] == "ORD-001"


def test_transform_orders_adds_partition_columns():
    sample_df = pd.DataFrame({
        "order_id": ["ORD-001"],
        "order_date": ["2024-01-01"],
        "customer_id": ["CUST-001"],
        "product_category": ["Electronics"],
        "order_amount": [1200.50],
        "quantity": [1],
        "country": ["USA"],
        "payment_status": ["paid"]
    })

    transformed_df = transform_orders(sample_df)

    assert "order_year" in transformed_df.columns
    assert "order_month" in transformed_df.columns
    assert transformed_df.iloc[0]["order_year"] == 2024
    assert transformed_df.iloc[0]["order_month"] == 1


def test_transform_orders_raises_error_for_missing_columns():
    sample_df = pd.DataFrame({
        "order_id": ["ORD-001"],
        "order_amount": [1200.50]
    })

    with pytest.raises(ValueError, match="Missing required columns"):
        transform_orders(sample_df)


def test_load_clean_orders_creates_output_file(tmp_path):
    sample_df = pd.DataFrame({
        "order_id": ["ORD-001"],
        "order_date": ["2024-01-01"],
        "customer_id": ["CUST-001"],
        "product_category": ["Electronics"],
        "order_amount": [1200.50],
        "quantity": [1],
        "country": ["USA"],
        "payment_status": ["paid"],
        "order_year": [2024],
        "order_month": [1]
    })

    output_file = tmp_path / "ecommerce_orders_clean.csv"

    load_clean_orders(sample_df, output_path=str(output_file))

    assert output_file.exists()

    loaded_df = pd.read_csv(output_file)
    assert len(loaded_df) == 1