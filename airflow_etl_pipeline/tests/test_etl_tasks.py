import sys
from pathlib import Path

import pandas as pd
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.etl_tasks import transform_orders, load_orders


def test_transform_orders_removes_missing_values():
    sample_df = pd.DataFrame({
        "order_id": ["ORD-001", "ORD-002"],
        "order_date": ["2024-01-01", "2024-01-02"],
        "customer_id": ["CUST-001", "CUST-002"],
        "order_amount": [120.50, None],
        "order_status": ["completed", "failed"]
    })

    transformed_df = transform_orders(sample_df)

    assert len(transformed_df) == 1
    assert transformed_df.iloc[0]["order_id"] == "ORD-001"


def test_transform_orders_removes_invalid_amounts():
    sample_df = pd.DataFrame({
        "order_id": ["ORD-001", "ORD-002", "ORD-003"],
        "order_date": ["2024-01-01", "2024-01-02", "2024-01-03"],
        "customer_id": ["CUST-001", "CUST-002", "CUST-003"],
        "order_amount": [120.50, 0, -25.00],
        "order_status": ["completed", "pending", "failed"]
    })

    transformed_df = transform_orders(sample_df)

    assert len(transformed_df) == 1
    assert transformed_df.iloc[0]["order_amount"] == 120.50


def test_transform_orders_raises_error_for_missing_columns():
    sample_df = pd.DataFrame({
        "order_id": ["ORD-001"],
        "order_amount": [120.50]
    })

    with pytest.raises(ValueError, match="Missing required columns"):
        transform_orders(sample_df)


def test_load_orders_creates_output_file(tmp_path):
    sample_df = pd.DataFrame({
        "order_id": ["ORD-001"],
        "order_date": ["2024-01-01"],
        "customer_id": ["CUST-001"],
        "order_amount": [120.50],
        "order_status": ["completed"]
    })

    output_file = tmp_path / "processed_customer_orders.csv"

    load_orders(sample_df, output_path=str(output_file))

    assert output_file.exists()

    loaded_df = pd.read_csv(output_file)
    assert len(loaded_df) == 1