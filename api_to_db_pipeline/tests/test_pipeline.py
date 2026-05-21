import sys
from pathlib import Path

import pandas as pd
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from src.transform import transform_users
from src.load import load_to_sqlite, validate_load


def test_transform_users_flattens_api_records():
    sample_records = [
        {
            "id": 1,
            "name": "Test User",
            "username": "testuser",
            "email": "test@example.com",
            "address": {
                "city": "Chicago",
                "zipcode": "60007"
            },
            "company": {
                "name": "Test Company"
            }
        }
    ]

    df = transform_users(sample_records)

    assert len(df) == 1
    assert "user_id" in df.columns
    assert "city" in df.columns
    assert "company_name" in df.columns
    assert df.iloc[0]["user_id"] == 1
    assert df.iloc[0]["city"] == "Chicago"
    assert df.iloc[0]["company_name"] == "Test Company"


def test_transform_users_raises_error_for_empty_records():
    with pytest.raises(ValueError, match="No records received"):
        transform_users([])


def test_load_and_validate_sqlite(tmp_path):
    sample_df = pd.DataFrame({
        "user_id": [1, 2],
        "name": ["User One", "User Two"],
        "username": ["userone", "usertwo"],
        "email": ["one@example.com", "two@example.com"],
        "city": ["Chicago", "Dallas"],
        "zipcode": ["60007", "75001"],
        "company_name": ["Company A", "Company B"]
    })

    test_db_path = tmp_path / "test_api_users.db"

    load_to_sqlite(sample_df, db_path=str(test_db_path), table_name="users")
    row_count = validate_load(db_path=str(test_db_path), table_name="users")

    assert row_count == 2
