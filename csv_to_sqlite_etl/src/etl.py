import pandas as pd
from db import get_connection

REQUIRED_COLUMNS = [
    "Order ID", "Order Date", "Ship Date", "Customer ID",
    "Sales", "Quantity", "Profit"
]

def extract(csv_path: str) -> pd.DataFrame:
    return pd.read_csv(csv_path, encoding="latin-1")

def transform(df: pd.DataFrame) -> pd.DataFrame:
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    
    df = df.dropna(subset=REQUIRED_COLUMNS).copy()

    df['Order Date'] = pd.to_datetime(df["Order Date"], errors='coerce')
    df["Ship Date"] = pd.to_datetime(df["Ship Date"], errors="coerce")
    df = df.dropna(subset=["Order Date", "Ship Date"])

    df.columns = [c.strip().lower().replace(" ", "_").replace("-","_") for c in df.columns]
    return df

def load(df: pd.DataFrame, db_path: str, table_name: str = "sales") -> None:
    with get_connection(db_path) as conn:
        df.to_sql(table_name, conn, if_exists="replace", index=False)

def run():
    csv_path = "data/superstore.csv"
    db_path = "output/superstore.db"

    print(f"Reading: {csv_path}")
    df_raw = extract(csv_path)
    print(f"Rows extracted: {len(df_raw)}")

    df_clean = transform(df_raw)
    print(f"Rows after transform: {len(df_clean)}")

    load(df_clean, db_path)
    print(f"Loaded into: {db_path}")

if __name__ == "__main__":
    run()