import pandas as pd
import os
import numpy as np
from dotenv import load_dotenv
from data_cleaner import clean_dataframe

load_dotenv()

payment_updater_file = os.getenv("PAYMENT_UPDATER_FILE")
df = pd.read_csv(payment_updater_file)

def transform_payment_mode():
    try:
        total_rows = len(df)
        print(f"Total rows in the dataset: {total_rows}")

        columns = df.columns
        print(f"Columns in the dataset: {columns}")

        unique_non_null_payment_values = df["Payment"].dropna().unique() # gpay, cash, card, amazon pay
        print(unique_non_null_payment_values)

        # Get top 2 most frequent payment options
        count_payment_values = df["Payment"].value_counts().head(2) # gpay 125, cash 75
        print(count_payment_values.to_string())

        val1, val2 = count_payment_values.index
        gpay, cash = count_payment_values.values[0], count_payment_values.values[1]
        print(f"Count of gpay transaction is -- {gpay}\nCount of cash transaction is -- {cash}")

        # Get null values of payment
        null_records = df["Payment"].isna().sum()

        # calculate fill
        total_payment_count = gpay + cash

        fill_gpay = int(round((gpay / total_payment_count) * null_records)) # calculate fill count for gpay
        fill_cash = null_records - fill_gpay # # calculate fill count for cash

        print(f"Fill null payment values {fill_gpay} of {null_records} with Gpay")
        print(f"Fill null payment values {fill_cash} of {null_records} with Cash")


        fill_values = [val1] * fill_gpay + [val2] * fill_cash

        np.random.shuffle(fill_values)

        df.loc[df["Payment"].isna(), "Payment"] = fill_values

        df["Payment"] = df["Payment"].str.replace("Gpay", "1").replace("Cash", "4").replace("Debit Card", "5").replace("Amazon Pay", "6")

        return df

    except Exception as e:
        print(f"Error in transforming payment mode: {e}")


def export_transformed_payment_mode():
    try:
        df = transform_payment_mode()
        data = clean_dataframe(df)

        output_file = "data/cleaned/payment_updater.csv"
        data.to_csv(output_file, index=False)
        print(f"Transformed payment mode data exported successfully to {output_file}")
    except Exception as e:  
        print(f"Error in exporting transformed payment mode data: {e}")


export_transformed_payment_mode()