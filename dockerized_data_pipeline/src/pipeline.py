from pathlib import Path

import pandas as pd


INPUT_PATH = "data/orders.csv"
OUTPUT_PATH = "output/cleaned_orders.csv"


def extract(input_path: str = INPUT_PATH) -> pd.DataFrame:
    """
    Read raw orders data from CSV.
    """
    return pd.read_csv(input_path)


def transform(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform raw orders data.
    """
    required_columns = [
        "order_id",
        "order_date",
        "customer_id",
        "amount",
        "status"
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    df = df.dropna(subset=required_columns).copy()

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df = df.dropna(subset=["order_date"])

    df = df[df["amount"] > 0]

    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    return df


def load(df: pd.DataFrame, output_path: str = OUTPUT_PATH) -> None:
    """
    Save cleaned orders data to CSV.
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def run_pipeline() -> None:
    """
    Run full ETL pipeline.
    """
    print("Starting dockerized data pipeline...")

    raw_df = extract()
    print(f"Rows extracted: {len(raw_df)}")

    clean_df = transform(raw_df)
    print(f"Rows after transformation: {len(clean_df)}")

    load(clean_df)
    print(f"Cleaned data saved to: {OUTPUT_PATH}")

    print("Pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()