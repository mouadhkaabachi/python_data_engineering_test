from os import listdir
from os.path import abspath, join

import pandas as pd

from src.common.logger import logger


def load_csv_files(folder, sep=","):
    """
    load all csv files to a dict
    """
    logger.info("Loading dataframes...")
    loaded_df = {}
    for file_name in listdir(abspath(folder)):
        if file_name.lower().endswith(".csv"):
            file_path = join(abspath(folder), file_name)
            loaded_df[file_name.replace(".csv", "")] = pd.read_csv(file_path, sep=sep)
    logger.info("Loading dataframes : SUCCESS")
    return loaded_df
