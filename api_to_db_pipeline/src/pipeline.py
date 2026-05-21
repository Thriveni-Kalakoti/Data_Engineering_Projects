from extract import extract_api_data
from transform import transform_users
from load import load_to_sqlite, validate_load


def run_pipeline() -> None:
    """
    Run the full API to database pipeline.
    """
    print("Starting API to database pipeline...")

    raw_records = extract_api_data()
    print(f"Records extracted: {len(raw_records)}")

    transformed_df = transform_users(raw_records)
    print(f"Rows transformed: {len(transformed_df)}")

    load_to_sqlite(transformed_df)
    print("Data loaded into SQLite database.")

    row_count = validate_load()
    print(f"Rows validated in database: {row_count}")

    if row_count != len(transformed_df):
        raise ValueError(
            f"Validation failed: expected {len(transformed_df)} rows, found {row_count}"
        )

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()