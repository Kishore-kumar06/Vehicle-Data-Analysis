import os
from src.data_operations.data_processing import get_transformed_files, clean_data

def main():
    curr_path = os.getcwd()
    output_folder = os.path.join(curr_path, "source_files", "cleaned_files")

    for file in get_transformed_files(curr_path):
        clean_data(file, output_folder)


if __name__ == "__main__":
    main()
