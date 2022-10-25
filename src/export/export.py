from src.common.logger import logger


def to_json(df, output_file):
    """
    roduire en sortie un fichier JSON qui représente
    un graphe de liaison entre les différents médicaments et leurs
    mentions respectives dans les différentes publications
    PubMed, les différentes publications scientifiques et enfin
    les journaux avec la date associée à chacune de ces mentions.
    """
    logger.info(f"Exporting result to {output_file} ...")
    df.groupby(["drug", "title", "date"])["journal"].sum().to_json(output_file)
    logger.info("Exporting result: SUCCESS")
