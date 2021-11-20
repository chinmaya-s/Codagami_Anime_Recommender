import pandas as pd
import json
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

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

studiosDF = pd.DataFrame(columns=['id', 'name', 'users', 'rating'])
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
studiosDF = studiosDF[~(studiosDF['users'] < 100)]

# These graphs are plotted with the condition that the data is
# sorted by the total number of animes with highest being at top
fig = studiosDF.plot(x='name', xlabel='Studios in decreasing order of number of animes',
                     y='animes', ylabel='Number of animes', title='Number of animes produced by each studio').get_figure()
ax = plt.gca()
ax.axes.xaxis.set_ticks([])
fig.savefig('outputs/plot_animes.jpeg')


fig = studiosDF.plot(x='name',
                     y='users').get_figure()
ax = plt.gca()
ax.axes.xaxis.set_ticks([])
plt.title('Average number of users for each studio', fontsize=20)
plt.xlabel('Studios in decreasing order of number of animes', fontsize=20)
plt.ylabel('Number of users', fontsize=20)
plt.yticks(fontsize=20)
fig.set_size_inches(14.5, 10, forward=True)
fig.savefig('outputs/plot_users.jpeg')


fig = studiosDF.plot(x='name', xlabel='Studios in decreasing order of number of animes',
                     y='rating', ylabel='Average Rating', title='Average rating of animes produced by each studio').get_figure()
ax = plt.gca()
ax.axes.xaxis.set_ticks([])
fig.savefig('outputs/plot_rating.jpeg')


topStudiosDF = studiosDF.head(n=20)

fig = topStudiosDF.plot(x='name', y='users', kind='bar', title='Average number of users of animes produced by top 20 studios',
                        ylabel='Average Number of Users', xlabel='Studios in decreasing order of number of animes').get_figure()
fig.set_size_inches(8, 8, forward=True)
plt.tight_layout()
fig.savefig('outputs/plot_users_top_studios.jpeg')

fig = topStudiosDF.plot(x='name', y='rating', kind='bar', title='Average rating of animes produced by top 20 studios',
                        ylabel='Average Rating', xlabel='Studios in decreasing order of number of animes').get_figure()
fig.set_size_inches(8, 8, forward=True)
plt.tight_layout()
fig.savefig('outputs/plot_rating_top_studios.jpeg')
