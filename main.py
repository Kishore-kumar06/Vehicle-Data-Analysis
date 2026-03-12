import os
from src.data_operations.data_processing import get_transformed_files, clean_data, fetch_data_for_uploads
from src.data_operations.file_operation import select_file
from src.crud_operations.database_operation import insert_records


def cleanning_data():
    try:
        curr_path = os.getcwd()
        output_folder = os.path.join(curr_path, "source_files", "cleaned_files")

        for file in get_transformed_files(curr_path):
            clean_data(file, output_folder)
    except Exception as ex:
        print(f"An error ocured while cleaning data.")

def upload_data():
    try:
        file_path = select_file()

        if file_path != '' or file_path is not None:
            data, table_name, column_names, place_holders =  fetch_data_for_uploads(file_path)

            insert_records(data, name=table_name, column_names=column_names, place_holders=place_holders)
        else:
            print(f'Selected file path is none')
       
    except Exception as ex:
        print(f"An error ocured while uploading data.")


def main():
    # cleanning_data()
    upload_data()
    
    

if __name__ == "__main__":
    main()
    
