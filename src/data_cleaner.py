import os
import pandas as pd

YES_NO_MAP = {"Yes": 1, "YES": 1, "yes": 1, "No": 0, "NO": 0, "no": 0}

def _convert_yes_no(value):
    """Convert Yes/No strings to 1/0. Leave other values unchanged."""
    if value in YES_NO_MAP:
        return YES_NO_MAP[value]
    if value == "":
        return None
    return value


def _is_text_column(series):
    """
    Return True if this column holds text values.
    Works in both pandas 2.x (dtype=object) and pandas 3.x (dtype=StringDtype).
    """
    return pd.api.types.is_string_dtype(series) or series.dtype == object


def clean_dataframe(df):
    """
    Apply standard cleaning to any dataframe:
    - Strip whitespace from column names
    - Strip whitespace from text columns
    - Replace Yes/No with 1/0
    - Parse date columns
    - Drop duplicates
    """
    # Clean column names
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    for col in df.columns:
        # Clean text columns
        if _is_text_column(df[col]):
            df[col] = df[col].astype(str).str.strip()
            df[col] = df[col].apply(_convert_yes_no)

        # Parse date columns automatically
        if "date" in col:
            df[col] = pd.to_datetime(df[col], errors="coerce")
            df[col] = df[col].dt.strftime("%Y-%m-%d")

    # Drop full duplicates
    df = df.drop_duplicates()

    return df


def load_cleaned_csv(folder, filename):
    """Load and clean a single CSV file."""
    filepath = os.path.join(folder, filename)
    df = pd.read_csv(filepath, encoding="utf-8")
    df = clean_dataframe(df)
    return df


def load_all_tables(folder):
    """
    Load all CSV files from the cleaned folder.
    Returns a dict: { table_name: dataframe }
    """
    tables = {}
    csv_files = [f for f in os.listdir(folder) if f.endswith(".csv")]

    for filename in csv_files:
        table_name = filename.replace(".csv", "")
        tables[table_name] = load_cleaned_csv(folder, filename)
        print(f"  Loaded: {table_name} ({len(tables[table_name])} rows)")

    return tables
