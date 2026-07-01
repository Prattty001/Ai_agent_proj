import pandas as pd
from datetime import datetime

def check_freshness(df):
    if "order_date" not in df.columns:
        return {
            "status": "WARNING",
            "details": "No order_date column found."
        }
    
#extracting teh latest date.
    latest = pd.to_datetime(df["order_date"]).max()

    return {
        "status": "PASS",
        "latest_record": str(latest)
    }