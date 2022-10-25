"""Main module."""
from os.path import isfile

from src.common.common import get_config
from src.common.logger import logger
from src.common.utils import get_top_journals
from src.export.export import to_json
from src.loader.loader import load_csv_files
from src.transform.transform import step1_generate_mentioned_drugs

config = get_config()
data_source_folder = config["DATA_SOURCE_FOLDER"]
sep = config["SEP"]
output_file = config["OUTPUT_FILE"]


def run():
    logger.info("Starting Pipeline ...")
    loaded_df = load_csv_files(data_source_folder, sep=sep)
    generated_df = step1_generate_mentioned_drugs(loaded_df)
    to_json(df=generated_df, output_file=output_file)
    logger.info("Pipeline Finished: SUCCESS")


def get_top(top):
    """
    Extraire depuis le json produit par la data pipeline le nom du journal
    qui mentionne le plus de médicaments différents
    """
    if not isfile(output_file):
        print("you need to run pipeline before")
        exit(0)
    return get_top_journals(output_file, top=top)
