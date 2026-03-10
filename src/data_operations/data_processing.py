import os
import pandas as pd


def get_transformed_files(curr_path):
    try:
        transformed_files_path = os.path.join(curr_path, 'source_files', 'transformed_files')

        for file in sorted(os.listdir(transformed_files_path)):
            if file.endswith(".csv"):
                yield os.path.join(transformed_files_path, file)

    except Exception as er:
        print(f"An error occurred while fetching transformed files: {er}")


def clean_column_names(df):
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(" ", "_")
                  .str.replace(r"[^\w]", "", regex=True)
    )
    return df


def clean_string_values(df):
    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype(str).str.strip()
        df[col] = df[col].str.title()
        df[col] = df[col].replace({"": pd.NA, "nan": pd.NA, "None": pd.NA})
    return df


def clean_data(input_file, output_folder):
    try:
        print(f"Reading file: {input_file}")

        df = pd.read_csv(input_file, encoding="utf-8", low_memory=False)

        # Standardize column names
        df = clean_column_names(df)

        # Clean string columns
        df = clean_string_values(df)

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Drop fully empty rows
        df = df.dropna(how="all")

        # Optional: reset index
        df = df.reset_index(drop=True)

        # Create output folder if not exists
        os.makedirs(output_folder, exist_ok=True)

        output_file = os.path.join(output_folder, os.path.basename(input_file))
        df.to_csv(output_file, index=False, encoding="utf-8")

        print(f"Cleaned file saved to: {output_file}")

    except Exception as ex:
        print(f"An error occurred while cleaning data in {input_file}: {ex}")

