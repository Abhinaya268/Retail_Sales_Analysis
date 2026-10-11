
from pathlib import Path
from getpass import getpass
from urllib.parse import quote

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


# Project folder and CSV file
PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_FILE = PROJECT_ROOT / "data" / "Sample - Superstore.csv"


# PostgreSQL connection settings
DB_USER = "postgres"
DB_HOST = "localhost"
DB_PORT = 5432
DB_NAME = "retail_sales_db"


def main():
    engine = None

    try:
        # Check whether the CSV file exists
        if not CSV_FILE.exists():
            print(f"CSV file not found: {CSV_FILE}")
            return

        # Read the CSV file
        print("Reading CSV file...")
        df = pd.read_csv(CSV_FILE, encoding="cp1252")

        print(f"CSV rows: {len(df)}")
        print(f"CSV columns: {len(df.columns)}")

        # Clean column names
        df.columns = [str(col).strip() for col in df.columns]

        # Map CSV column names to PostgreSQL column names
        column_map = {
            "Row ID": "row_id",
            "Order ID": "order_id",
            "Order Date": "order_date",
            "Ship Date": "ship_date",
            "Ship Mode": "ship_mode",
            "Customer ID": "customer_id",
            "Customer Name": "customer_name",
            "Segment": "segment",
            "Country": "country",
            "City": "city",
            "State": "state",
            "Postal Code": "postal_code",
            "Region": "region",
            "Product ID": "product_id",
            "Category": "category",
            "Sub-Category": "sub_category",
            "Product Name": "product_name",
            "Sales": "sales",
            "Quantity": "quantity",
            "Discount": "discount",
            "Profit": "profit",
        }

        # Check that all expected CSV columns exist
        missing = set(column_map) - set(df.columns)

        if missing:
            print("Missing CSV columns:", sorted(missing))
            print("Actual CSV headers:", df.columns.tolist())
            return

        # Keep the expected columns and rename them
        df = df[list(column_map.keys())].rename(columns=column_map)

        # Convert dates; the CSV may contain multiple date formats
        for col in ["order_date", "ship_date"]:
            df[col] = pd.to_datetime(
                df[col],
                format="mixed",
                errors="raise"
            ).dt.date

        # Convert numeric columns
        for col in ["sales", "discount", "profit"]:
            df[col] = pd.to_numeric(
                df[col].astype(str).str.replace("%", "", regex=False),
                errors="raise"
            )

        # Superstore discount values are stored as percentages.
        # Convert values such as 20 to 0.20 for PostgreSQL.
        df["discount"] = df["discount"] / 100

        # Convert integer columns
        df["row_id"] = pd.to_numeric(
            df["row_id"], errors="raise"
        ).astype(int)

        df["quantity"] = pd.to_numeric(
            df["quantity"], errors="raise"
        ).astype(int)

        # Preserve postal codes as text
        df["postal_code"] = df["postal_code"].astype("string")

        # Ask for the PostgreSQL password without displaying it
        db_password = getpass("Enter your PostgreSQL password: ")

        # Build a connection URL safely, including special characters
        connection_url = URL.create(
            drivername="postgresql+psycopg",
            username=DB_USER,
            password=db_password,
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
        )

        engine = create_engine(connection_url)

        # Verify the connection before changing the table
        with engine.connect() as connection:
            current_db = connection.execute(
                text("SELECT current_database()")
            ).scalar_one()

            if current_db != DB_NAME:
                raise RuntimeError(
                    f"Connected to unexpected database: {current_db}"
                )

        print("PostgreSQL connection successful.")
        print("Importing data...")

        # Import transactionally so a failed import can roll back
        with engine.begin() as connection:
            connection.execute(
                text("TRUNCATE TABLE public.retail_sales")
            )

            df.to_sql(
                "retail_sales",
                connection,
                schema="public",
                if_exists="append",
                index=False,
                chunksize=1000,
                method="multi",
            )

            result = connection.execute(
                text("SELECT COUNT(*) FROM public.retail_sales")
            ).scalar_one()

        print("Import successful!")
        print(f"Rows imported: {result}")

        if result == len(df):
            print("Verification passed: all CSV rows were imported.")
        else:
            print("Warning: the database row count differs from the CSV.")

    except Exception as error:
        print("Import failed:")
        print(f"{type(error).__name__}: {error}")

    finally:
        if engine is not None:
            engine.dispose()


if __name__ == "__main__":
    main()
