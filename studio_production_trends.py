import pandas as pd
import json
from pathlib import Path

################################################################
# Add the names of animes here for which graph is needed
names_list = ['Toei Animation', 'Sunrise',
              'J.C.Staff', 'Madhouse', 'Production I.G']
################################################################
# Code to load data
# pathlist = Path('data').rglob('*.json')
# df_list = []
# for path in pathlist:
#     # because path is object not string
#     path_in_str = str(path)
#     json_file = open(path_in_str)
#     data = json.load(json_file)
#     df = pd.DataFrame.from_dict(data, orient='index')
#     df_list.append(df)
# pathlist = Path('data').rglob('*.json')
df_list = []
# for path in pathlist:
    # because path is object not string
# path_in_str = str(path)
json_file = open('data/anime_list_final_231.json')
data = json.load(json_file)
df = pd.DataFrame.from_dict(data, orient='index')
df_list.append(df)
    #  print(path_in_str)

df = pd.concat(df_list, axis=1)

# Preprocess data
df = df.dropna(subset=['id'])

# Creating new Studio centric dataframe
studiosDF = pd.DataFrame(columns=['name', 'start_date'])

# using num_list_users for users
idxCount = 0
for idx, row in df.iterrows():
    for x in row['studios']:
        if x['name'] in names_list:
            studiosDF.loc[idxCount] = [x['name'], row['start_date']]
            idxCount = idxCount + 1

# Preprocess Studio dataframe
studiosDF['start_date'] = pd.to_datetime(studiosDF['start_date'])
studiosDF['start_date'] = studiosDF['start_date'].dt.year
studiosDF.dropna(inplace=True)
studiosDF['start_date'] = studiosDF['start_date'].astype(int)
studiosDF = studiosDF[~(studiosDF['start_date'] > 2021)]

# transforming dataframe so that it is easy to plot
plotDF = pd.crosstab([studiosDF['name']], studiosDF['start_date'])
plotDF = plotDF.reset_index()
plotDF.rename(columns={'name': 'Studio'}, inplace=True)
plotDF = plotDF.set_index(plotDF['Studio'])
plotDF.drop('Studio', axis=1, inplace=True)
plotDF = plotDF.transpose()

fig = plotDF.plot(title='Number of animes produced by top studios each year',
                  ylabel='Number of animes produced',
                  xlabel='Year of production',
                  legend=True, kind='line').get_figure()
fig.set_size_inches(14.5, 8.5, forward=True)
fig.savefig('outputs/plot_anime_vs_year.jpeg')
