import pandas as pd
import numpy as np
import json

INP_DIR = 'data/'
OUT_DIR = 'outputs/'

# get data from json in a dataframe
path_in_str = 'anime_list_final_231.json'
json_file = open(INP_DIR+path_in_str)
data = json.load(json_file)
df = pd.DataFrame.from_dict(data, orient='index')

df = df[['source', 'rank', 'num_list_users']]
df.dropna(inplace=True)
df['rank'] = df['rank'].astype(int)
df = df[df['rank'] > 0]


# get source vs popularity plot
df_source_pop = df[['source','num_list_users']]
df_source_pop = df_source_pop.groupby('source').agg({'num_list_users': 'sum'}).reset_index()

fig = df_source_pop.plot(x='source', 
                        y='num_list_users', 
                        xlabel='Source', 
                        ylabel='Total No of Users', 
                        kind='bar', 
                        title = 'Total Number of Viewers vs Source', 
                        rot=-45, 
                        figsize=(15,12)).get_figure()
fig.savefig(OUT_DIR+'source_vs_popularity.jpg')


# get source vs rating plot
df_source_rating = df[['source','rank']]
df_source_rating_mean = df_source_rating.groupby('source').agg({'rank': 'mean'}).reset_index()
source_list = np.unique(df_source_rating_mean['source'])
print(source_list)
df_source_rating_mean.sort_values(['rank'], ascending=True, axis=0, inplace=True)
source_list_ordered = df_source_rating_mean['source'].to_list()
pos_list = [source_list_ordered.index(k) for k in source_list ]
print(pos_list)

axes = df_source_rating.boxplot('rank',
                        by='source',
                        grid=False,
                        positions=pos_list,
                        showfliers=False,
                        rot=-45, 
                        figsize=(15,12))
axes.set_xlabel('Source')
axes.set_ylabel('Rank')
axes.set_title('Source vs Ranking')
fig = axes.get_figure()
fig.suptitle('')
fig.savefig(OUT_DIR+'source_vs_ranking.jpg')