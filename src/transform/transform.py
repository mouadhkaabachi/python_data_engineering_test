import pandas as pd


def generate_mentioned_drugs(dataframes, df_to_check, column_to_check):

    drugs = dataframes['drugs']['drug'].to_list()
    df_to_check = dataframes[df_to_check]
    for drug in drugs:
        df_to_check.loc[df_to_check[column_to_check].str.contains(drug, case=False), "drug"] = drug
    return df_to_check[df_to_check["drug"].notna()]


def step1_generate_mentioned_drugs(loaded_df):
    pubmed_drugs_df = generate_mentioned_drugs(loaded_df, df_to_check="pubmed", column_to_check="title")
    clinical_trials_df = generate_mentioned_drugs(loaded_df, df_to_check="clinical_trials",
                                                  column_to_check="scientific_title").rename(
        columns={"scientific_title": "title"})
    return pd.concat([pubmed_drugs_df, clinical_trials_df])


def step11(dataframes):
    drugs = dataframes['drugs']['drug'].to_list()
    pubmed_df = dataframes['pubmed']
    for drug in drugs:
        pubmed_df.loc[pubmed_df['title'].str.contains(drug, case=False), drug] = True
    pubmed_df = pubmed_df.dropna(axis=1, how="all")
    pubmed_df.to_csv('aaaaaaa2.csv')
    # pubmed_df[drug] = pubmed_df['title'].str.contains(drug, case=False).any()
    # print(pubmed_df[drug])
    # pubmed_df = pubmed_df[pubmed_df[drug] == True]
    # print('llllllllllll')
    #
    # print(pubmed_df['title'])


def step11(dataframes):
    drugs = dataframes['drugs']['drug'].to_list()
    df = pd.DataFrame(columns=dataframes['pubmed'].columns)
    for drug in drugs:
        for index, row in dataframes['pubmed'].iterrows():
            if drug.lower() in row['title'].lower():
                row['drug'] = drug
                df = df.append(row, ignore_index=True)

    df.to_csv('aaaaaaa.csv')
    # pubmed_df[drug] = pubmed_df['title'].str.contains(drug, case=False).any()
    # print(pubmed_df[drug])
    # pubmed_df = pubmed_df[pubmed_df[drug] == True]
    # print('llllllllllll')
    #
    # print(pubmed_df['title'])
