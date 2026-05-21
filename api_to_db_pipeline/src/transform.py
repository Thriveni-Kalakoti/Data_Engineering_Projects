import pandas as pd


def transform_users(records: list[dict]) -> pd.DataFrame:
    """
    Transform raw API user records into a clean tabular DataFrame.

    Args:
        records: List of dictionaries returned from the API.

    Returns:
        Clean pandas DataFrame ready for database loading.
    """
    if not records:
        raise ValueError("No records received for transformation.")

    df = pd.json_normalize(records)

    selected_columns = [
        "id",
        "name",
        "username",
        "email",
        "address.city",
        "address.zipcode",
        "company.name"
    ]

    missing_columns = [col for col in selected_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing expected columns: {missing_columns}")

    df = df[selected_columns].copy()

    df = df.rename(columns={
        "id": "user_id",
        "address.city": "city",
        "address.zipcode": "zipcode",
        "company.name": "company_name"
    })

    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    df = df.dropna(subset=["user_id", "name", "email"])

    return df


if __name__ == "__main__":
    from extract import extract_api_data

    raw_records = extract_api_data()
    transformed_df = transform_users(raw_records)

    print(f"Rows transformed: {len(transformed_df)}")
    print(transformed_df.head())