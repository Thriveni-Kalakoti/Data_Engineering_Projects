from pathlib import Path

import pandas as pd


INPUT_PATH = "data/customer_orders.csv"
OUTPUT_PATH = "output/processed_customer_orders.csv"


def extract_orders(input_path: str = INPUT_PATH) -> pd.DataFrame:
    """
    Extract customer order data from a CSV file.
    """
    return pd.read_csv(input_path)


def transform_orders(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform customer order data.
    """
    required_columns = [
        "order_id",
        "order_date",
        "customer_id",
        "order_amount",
        "order_status"
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    df = df.dropna(subset=required_columns).copy()

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df = df.dropna(subset=["order_date"])

    df = df[df["order_amount"] > 0]

    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    return df


def load_orders(df: pd.DataFrame, output_path: str = OUTPUT_PATH) -> None:
    """
    Load processed order data into an output CSV file.
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def run_etl_pipeline() -> None:
    """
    Run the full ETL pipeline.
    """
    print("Starting Airflow ETL pipeline task logic...")

    raw_df = extract_orders()
    print(f"Rows extracted: {len(raw_df)}")

    clean_df = transform_orders(raw_df)
    print(f"Rows after transformation: {len(clean_df)}")

    load_orders(clean_df)
    print(f"Processed data saved to: {OUTPUT_PATH}")

    print("ETL task logic completed successfully.")


if __name__ == "__main__":
    run_etl_pipeline()