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
source_rename = {'4_koma_manga': '4-Koma Manga', 'book' : 'Book', 'card_game' : 'Card Game', 'digital_manga': 'Digital Manga', 'game':'Game', 'light_novel': 'Light Novel', 'manga': 'Manga', 'music': 'Music', 'novel': 'Novel', 'original': 'Original', 'other': 'Other', 'picture_book': 'Picture Book', 'radio': 'Radio', 'visual_novel': 'Visual Novel', 'web_manga': 'Web Manga'}
df = df.replace({'source': source_rename})


# get source vs popularity plot
df_source_pop = df[['source','num_list_users']]
df_source_pop = df_source_pop.groupby('source').agg({'num_list_users': 'mean'}).reset_index()

df_source_pop.rename(columns = {'num_list_users':'avg_no_users'}, inplace = True)

axes = df_source_pop.plot(x='source', 
                        y='avg_no_users', 
                        kind='bar',
                        rot=-45, 
                        figsize=(15,12))
axes.set_xlabel('Source', fontsize=18)
axes.set_ylabel('Average No of Users', fontsize=18)
axes.set_title('Average Number of Viewers vs Source', fontsize=22)
fig = axes.get_figure()
fig.suptitle('')
fig.savefig(OUT_DIR+'source_vs_popularity.jpg')


# get source vs rating plot
df_source_rating = df[['source','rank']]
df_source_rating_mean = df_source_rating.groupby('source').agg({'rank': 'mean'}).reset_index()
source_list = np.unique(df_source_rating_mean['source'])
df_source_rating_mean.sort_values(['rank'], ascending=True, axis=0, inplace=True)
source_list_ordered = df_source_rating_mean['source'].to_list()
pos_list = [source_list_ordered.index(k) for k in source_list ]

axes = df_source_rating.boxplot('rank',
                        by='source',
                        grid=False,
                        positions=pos_list,
                        showfliers=False,
                        rot=-45, 
                        figsize=(15,12))
axes.set_xlabel('Source', fontsize=18)
axes.set_ylabel('Rank', fontsize=18)
axes.set_title('Source vs Ranking', fontsize=22)
fig = axes.get_figure()
fig.suptitle('')
fig.savefig(OUT_DIR+'source_vs_ranking.jpg')