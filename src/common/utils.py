import json
from collections import Counter


def get_top_journals(output_file, top=1):
    """
    Extraire depuis le json produit par la data pipeline
    le nom du journal qui mentionne le plus de médicaments différents
    """
    with open(output_file) as json_file:
        data = json.load(json_file)
        word_dict = Counter(data.values())
        return word_dict.most_common(top)
