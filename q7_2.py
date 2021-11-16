import pandas as pd
import json
from pathlib import Path

###############################################################################
# Add the names of animes here for which graph is needed
names_list = ['Toei Animation', 'Sunrise', 'J.C.Staff']
###############################################################################
# Code to load data
pathlist = Path('data').rglob('*.json')
df_list = []
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    json_file = open(path_in_str)
    data = json.load(json_file)
    df = pd.DataFrame.from_dict(data, orient='index')
    df_list.append(df)

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
studiosDF['start_date'] = (studiosDF['start_date']//10)*10

# transforming dataframe so that it is easy to plot
plotDF = pd.crosstab([studiosDF['name']], studiosDF['start_date'])
plotDF = plotDF.reset_index()

for idx, row in plotDF.iterrows():
    titleName = row['name']
    row = row.drop(['name'])
    fig = row.plot(kind='bar', title=titleName,
                   ylabel='Number of animes made', xlabel='Decades').get_figure()
    fig.set_size_inches(14.5, 8.5, forward=True)
    fig.savefig('plot_'+titleName+'.jpeg')
