"""Functions for direct interactions with the raw data"""

import os
import pandas as pd

from ..filenames import DATA_PATH


def load_data(filename="aviation"):
    """Load raw CSV data from the project datastore

    :parameters:
    filename: str (default: "aviation")
      Filename of the data (without the .csv extension)

    :returns:
    pd.DataFrame object with the loaded data
    """
    filepath = construct_data_filepath(filename)
    return pd.read_csv(filepath)


def save_data(data, output):
    """Save data to a CSV file in the project data/ folder

    :parameters:
    data: pd.DataFrame
      Pandas DataFrame containing the data to be saved
    output: str
      Output filename (without extension) for the CSV data
    """
    filepath = construct_data_filepath(output)
    data.to_csv(filepath, index=False)


def construct_data_filepath(filename="raw_data"):
    """Construct filepath to data CSV file

    :parameters:
    filename: str (default: "raw_data")
      Filename of the data (without the .csv extension)

    :returns:
    str with the full filepath for loading and writing the data
    """
    file = f"{filename}.csv"
    return os.path.join(DATA_PATH, file)
