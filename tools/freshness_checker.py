import pandas as pd
from datetime import datetime


def check_freshness(df):

    if "order_date" not in df.columns:

        return {
            "status": "WARNING",
            "details": "No order_date column found."
        }

    try:

        dates = pd.to_datetime(
            df["order_date"],
            errors="coerce"
        )

        latest = dates.max()

        if pd.isna(latest):

            return {

                "status": "FAIL",

                "details": "Unable to parse order_date column."

            }

        today = pd.Timestamp.now()

        days_old = int(
            (today - latest).days
        )

        if days_old <= 30:

            status = "PASS"

        elif days_old <= 90:

            status = "WARNING"

        else:

            status = "FAIL"

        return {

            "status": status,

            "latest_record": str(latest),

            "days_old": days_old

        }

    except Exception as e:

        return {

            "status": "FAIL",

            "details": str(e)

        }