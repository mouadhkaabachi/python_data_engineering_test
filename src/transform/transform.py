import pandas as pd


def generate_mentioned_drugs(dataframes, df_to_check, column_to_check):
    """
    - Un drug est considéré comme mentionné dans
    un article PubMed ou un essai clinique s’il est mentionné
    dans le titre de la publication.
    - Un drug est considéré comme mentionné par un journal s’il
    est mentionné dans une publication émise par ce journal.
    """
    drugs_df = dataframes["drugs"]
    df = dataframes[df_to_check]

    drugs_df["join"] = 1
    df["join"] = 1

    cross_joined_df = df.merge(drugs_df, on="join").drop("join", axis=1)

    drugs_df.drop("join", axis=1, inplace=True)

    cross_joined_df["match"] = cross_joined_df.apply(
        lambda x: x[column_to_check].lower().find(x.drug.lower()), axis=1
    ).ge(0)

    return cross_joined_df[cross_joined_df["match"]].drop(
        ["match", "atccode", "id"], axis=1, errors="ignore"
    )


def step1_generate_mentioned_drugs(loaded_df):
    """
    - Un drug est considéré comme mentionné dans
    un article PubMed ou un essai clinique s’il est mentionné dans
    le titre de la publication.
    - Un drug est considéré comme mentionné par un journal
    s’il est mentionné dans une publication émise par ce journal.
    """
    pubmed_drugs_df = generate_mentioned_drugs(
        loaded_df, df_to_check="pubmed", column_to_check="title"
    )

    clinical_trials_df = generate_mentioned_drugs(
        loaded_df, df_to_check="clinical_trials", column_to_check="scientific_title"
    ).rename(columns={"scientific_title": "title"})

    df = pd.concat([pubmed_drugs_df, clinical_trials_df])

    # Un drug est considéré comme mentionné par
    # un journal s’il est mentionné dans une publication
    # émise par ce journal.
    df = df[df["journal"].notnull()]

    return df
