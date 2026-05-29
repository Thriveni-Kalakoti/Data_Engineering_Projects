from pathlib import Path

import pandas as pd


INPUT_PATH = "data/ecommerce_orders.csv"
OUTPUT_PATH = "output/ecommerce_orders_clean.csv"


def extract_orders(input_path: str = INPUT_PATH) -> pd.DataFrame:
    """
    Extract raw ecommerce orders data from CSV.
    """
    return pd.read_csv(input_path)


def transform_orders(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and prepare ecommerce orders data for cloud warehouse loading.
    """
    required_columns = [
        "order_id",
        "order_date",
        "customer_id",
        "product_category",
        "order_amount",
        "quantity",
        "country",
        "payment_status"
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    df = df.dropna(subset=required_columns).copy()

    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df = df.dropna(subset=["order_date"])

    df = df[df["order_amount"] > 0]
    df = df[df["quantity"] > 0]

    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    df["order_year"] = df["order_date"].dt.year
    df["order_month"] = df["order_date"].dt.month

    return df


def load_clean_orders(df: pd.DataFrame, output_path: str = OUTPUT_PATH) -> None:
    """
    Save cleaned ecommerce orders data as a warehouse-ready CSV.
    """
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)


def run_pipeline() -> None:
    """
    Run full cloud warehouse preparation pipeline.
    """
    print("Starting cloud data warehouse preparation pipeline...")

    raw_df = extract_orders()
    print(f"Rows extracted: {len(raw_df)}")

    clean_df = transform_orders(raw_df)
    print(f"Rows after transformation: {len(clean_df)}")

    load_clean_orders(clean_df)
    print(f"Clean warehouse-ready data saved to: {OUTPUT_PATH}")

    print("Cloud warehouse preparation pipeline completed successfully.")


if __name__ == "__main__":
    run_pipeline()