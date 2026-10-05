# %%
import pandas as pd
import logging
import sys
import os
from sqlalchemy import create_engine

# %%
db_host="localhost",
db_user="root",       
db_password="password",
db_name="e-commerce"


engine = create_engine(f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}")

# %%
logging.basicConfig(
    filename='etl_log.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# %%
def extract_data(csv_files, json_files):
    csv_data = {} 
    json_data = {}

    # CSV files
    for file in csv_files:
        table_name = file.split('.')[0]
        csv_data[table_name] = pd.read_csv(file)

    # JSON files
    for file in json_files:
        table_name = file.split('.')[0]
        json_data[table_name] = pd.read_json(file)

    return csv_data, json_data


# %%
def load_data(df_csv, df_json):
    try:
        with engine.connect() as conn:
            for table_name, df in {**df_csv, **df_json}.items():
                df.to_sql(table_name, conn, if_exists="replace", index=False)
                logging.info(f"✅ Loaded {table_name} into database.")
    except Exception as e:
        logging.error(f"❌ Error loading data: {e}")

# %%
def main():
    logging.info("ETL process started.")

    csv_files = ["orders.csv", "order_items.csv", "website_pageviews.csv", "website_sessions.csv"]
    json_files = ["order_item_refunds.json", "products.json"]

    df_csv, df_json = extract_data(csv_files, json_files)
    load_data(df_csv, df_json)

    logging.info("ETL process completed successfully.")

if __name__ == "__main__":
    main()

# %%
if __name__ == "__main__":
    main()


