# %%
import pandas as pd
import json
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import itertools

# %%


def savePlot(plot, name):
    fig = plot.get_figure()
    fig.savefig("outputs/" + name + '.jpeg', bbox_inches='tight')


# %%
path_in_str = 'data/anime_list_final_231.json'
json_file = open(path_in_str)
data = json.load(json_file)
df = pd.DataFrame.from_dict(data, orient='index')
df = df[df['error'] != 'not_found']
df.dropna(subset=['genres'], inplace=True)
df['start_date'] = pd.to_datetime(df['start_date'])
df = df[df['start_date'].dt.year < 2022]

def melt_series(s):
    lengths = s.str.len().values
    flat = [i for i in itertools.chain.from_iterable(s.values.tolist())]
    idx = np.repeat(s.index.values, lengths)
    return pd.Series(flat, idx, name=s.name)


df = melt_series(df.genres).to_frame().join(df.drop('genres', 1))
df.reset_index(inplace=True)


# %%
df['genre_name'] = df['genres'].apply(lambda x: x['name'])
df['genre_id'] = df['genres'].apply(lambda x: x['id'])

# %%
df1 = df.groupby(['start_date', 'genre_name'], as_index=False)['id'].count()
df1.rename({'id': 'anime_count'}, axis=1, inplace=True)
df1 = df1.pivot(index='start_date', columns='genre_name', values='anime_count')

# df1 = df1[['Action', 'Adventure', 'Avant Garde', 'Comedy', 'Demons',
#            'Drama', 'Ecchi', 'Fantasy', 'Hentai', 'Historical', 'Kids', 'Mecha', 'Military', 'Music',
#            'Mystery', 'Parody', 'Romance',
#            'School', 'Sci-Fi', 'Seinen', 'Shoujo', 'Shounen', 'Slice of Life',
#            'Space', 'Sports', 'Super Power', 'Supernatural']]

df1 = df1[['Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy',
            'Hentai', 'Historical', 'Kids', 'Music', 'Romance',
           'School', 'Sci-Fi', 'Shounen', 'Slice of Life', 'Supernatural']]

# %%
plot = df1.groupby([(df1.index.year)]).sum().plot(
    title='Number of anime started by genre per year', figsize=(10, 10), ylabel="Number of anime", xlabel="Year")
savePlot(plot, 'genre_num_anime_vs_year')

# %%

df2 = df.groupby(['genre_name'])['popularity'].mean().sort_values()
# df2 = df2[['Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy',
#             'Hentai', 'Historical', 'Kids', 'Music', 'Romance',
#            'School', 'Sci-Fi', 'Shounen', 'Slice of Life', 'Supernatural']]
savePlot(df2.plot(kind='bar', title='Mean popularity per genre', figsize=(10, 10), ylabel="Mean Popularity", xlabel="Genre"),
         'genre_vs_popularity')

# %%


def generateHistogram(field, yname):
    df2 = df.groupby(['genre_name'])[field].mean().sort_values()
    savePlot(df2.plot(kind='bar', title='Mean ' +
             yname + ' per genre', xlabel='Genre', ylabel=yname, figsize=(10, 10)), 'genre_vs_' + field)


# %%
df3 = df.groupby(['genre_name'])['id'].count()
df3 = df3[['Action', 'Adventure', 'Comedy', 'Drama', 'Fantasy',
           'Hentai', 'Historical', 'Kids', 'Music', 'Romance',
           'School', 'Sci-Fi', 'Shounen', 'Slice of Life', 'Supernatural']]
savePlot(df3.plot(kind='bar', title='Number of anime by genre', figsize=(
    10, 10), ylabel="Number of anime", xlabel="Genre"), 'genre_count')

# %%
# plot_fields = [('mean', 'Mean'),
#             ('rank', 'Rank'),
#             ('num_list_users', 'Number of users'),
#             ('num_episodes', 'Number of episodes'),
#             ('average_episode_duration', 'Average episode duration')]
# for field, ylabel1 in plot_fields:
#     generateHistogram(field, ylabel1)


df_rank = df.groupby(['genre_name'])['rank'].mean()
df_pop = df.groupby(['genre_name'])['popularity'].mean()
df_pop.index
frame = {'rank': df_rank, 'popularity': df_pop, 'genre_name': df_pop.index}
df4 = pd.DataFrame(frame)
df4
savePlot(df4.plot(kind='bar', x='genre_name', y=['rank', 'popularity'], figsize=(
    10, 10), ylabel="Value of rank/popularity", xlabel="Genre"), 'genre_vs_rank_and_pop')
# savePlot(df2.plot(kind='bar', title='Mean ' + yname + ' per genre', xlabel='Genre', ylabel=yname, figsize=(10,10)), 'genre_vs_' + field)
