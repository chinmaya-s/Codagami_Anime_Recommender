import pandas as pd
import json
from pathlib import Path
import numpy as np

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

studiosDF = pd.DataFrame(columns=['id', 'name', 'users', 'rating'])
# use num_list_users for users
idxCount = 0
for idx, row in df.iterrows():
    for x in row['studios']:
        studiosDF.loc[idxCount] = [x['id'], x['name'],
                                   row['statistics']['num_list_users'], row['mean']]
        idxCount = idxCount + 1
studiosDF['animes'] = studiosDF.groupby(['id'])['id'].transform('count')

studiosDF = studiosDF.groupby(['id', 'name', 'animes'], as_index=False).agg({
    'users': np.mean, 'rating': np.mean})
studiosDF.sort_values('animes', ascending=False, inplace=True)
studiosDF.dropna(subset=['users', 'rating'], inplace=True)

# These graphs are plotted with the condition that the data is
# sorted by the total number of animes with highest being at top
fig = studiosDF.plot(x='name', y='animes').get_figure()
fig.set_size_inches(14.5, 8.5, forward=True)
fig.savefig('plot_animes.jpeg')

fig = studiosDF.plot(x='name', y='users').get_figure()
fig.set_size_inches(14.5, 8.5, forward=True)
fig.savefig('plot_users.jpeg')

fig = studiosDF.plot(x='name', y='rating').get_figure()
fig.set_size_inches(14.5, 8.5, forward=True)
fig.savefig('plot_rating.jpeg')

topStudiosDF = studiosDF.head(n=20)

fig = topStudiosDF.plot(x='name', y='animes').get_figure()
fig.set_size_inches(14.5, 8.5, forward=True)
fig.savefig('plot_animes_top_studios.jpeg')

fig = topStudiosDF.plot(x='name', y='users').get_figure()
fig.set_size_inches(14.5, 8.5, forward=True)
fig.savefig('plot_users_top_studios.jpeg')

fig = topStudiosDF.plot(x='name', y='rating').get_figure()
fig.set_size_inches(14.5, 8.5, forward=True)
fig.savefig('plot_rating_top_studios.jpeg')
