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


def clean_dataframe(df):
    df.columns = (
        df.columns.str.strip()
                  .str.lower()
                  .str.replace(" ", "_")
                  .str.replace(r"[^\w]", "", regex=True)
    )

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].str.strip()
        df[col] = df[col].replace({"Yes": 1, "YES": 1, "No": 0, "NO": 0})
        df[col] = df[col].replace({"": pd.NA, "nan": pd.NA, "None": pd.NA})

        if "date" in col.lower():
            df[col] = pd.to_datetime(df[col], format="%d-%m-%Y", errors="coerce")
            df[col] = df[col].dt.strftime("%Y-%m-%d")

    df = df.drop_duplicates().reset_index(drop=True)
    df = df.dropna()
    return df



def clean_data(input_file, output_folder):
    try:
        print(f"Reading file: {input_file}")

        df = pd.read_csv(input_file, encoding="utf-8", low_memory=False)

        df = clean_dataframe(df)
        
        # Create output folder if not exists
        os.makedirs(output_folder, exist_ok=True)

        output_file = os.path.join(output_folder, os.path.basename(input_file))
        df.to_csv(output_file, index=False, encoding="utf-8")

        print(f"Cleaned file saved to: {output_file}")

    except Exception as ex:
        print(f"An error occurred while cleaning data in {input_file}: {ex}")


def fetch_data_for_uploads(file):
    try:
        data = pd.read_csv(file, encoding='UTF-8', index_col=False)
        table_name = os.path.basename(file).split('.')[0]

        if len(data.columns[0]) > 0:
            column = data.columns.to_list()
            column_names = ', '.join(column)
            place_holders = ', '.join(["%s"] * len(column))

            return data, table_name, column_names, place_holders

    except Exception as ex:
        print(f"An error occurred while fetching cleaned data for {file}: {ex}")