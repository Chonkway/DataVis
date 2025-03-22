import zipfile, os
import pandas as pd
from pathlib import Path

#Scripts for processing datasets scraped by Selenium script



def decompress(dir_name):
    """
    :param dir_name: directory of scraped WHO data

    Will create a temp directory and process data scraped from the WHO
    """

    # Define temp path to create if not existing
    temp_path = "C:\\Users\\Sable\\PyCharmMiscProject\\temp\\uncompress"
    os.makedirs(temp_path, exist_ok=True)

    # Iterate through files in the provided directory
    for file_name in os.listdir(dir_name):
        file_path = os.path.join(dir_name, file_name)

        # Check if it's a zip file
        if os.path.isfile(file_path) and file_path.endswith('.zip'):
            with zipfile.ZipFile(file_path, 'r') as who_data:
                print(f"Processing: {file_path}")
                who_data.extractall(temp_path)  # Extract all contents to the temp folder



def process_who_data(directory):
    """
    :param directory: the directory with all the uncompressed data
    """

    #Establish list of several data frames
    data_frames = []

    # Walk through the directory tree
    base_path = Path(directory)
    for folder in base_path.rglob('*'):
        if folder.is_dir():
            # Check if there are CSV files in the folder
            for file in folder.iterdir():
                if file.is_file() and file.suffix == '.csv':
                    # Load the identified CSV file into a DataFrame
                    print(f"Loading CSV file: {file}")
                    df = pd.read_csv(file)  # Load CSV into DataFrame
                    data_frames.append(df)  # Append to the list of DataFrames



        # Concatenate all df in list to one large df
        pd.concat(data_frames, ignore_index=True)
        print(data_frames)




process_who_data("C:\\Users\\Sable\\PyCharmMiscProject\\temp\\uncompress")


