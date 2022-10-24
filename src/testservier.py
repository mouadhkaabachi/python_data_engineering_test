"""Main module."""

from src.common.common import get_config
from src.loader.loader import load_csv_files
from src.transform.transform import step1_generate_mentioned_drugs

config = get_config()
data_source_folder = config['DATA_SOURCE_FOLDER']
sep = config['SEP']

loaded_df = load_csv_files(data_source_folder, sep=sep)

print(step1_generate_mentioned_drugs(loaded_df))

