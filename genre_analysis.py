from matplotlib import colors
from numpy.core.fromnumeric import mean
import pandas as pd
import json
import matplotlib.pyplot as plt

INP_DIR = 'data/'
OUT_DIR = 'outputs/'

# get data from json in a dataframe
path_in_str = 'anime_list_final_231.json'
json_file = open(INP_DIR+path_in_str)
data = json.load(json_file)
df = pd.DataFrame.from_dict(data, orient='index')
# print(df.columns)

df = df[['genres', 'num_list_users']]
df.dropna(inplace=True)

# change genres column
df_dict_to_list = [[x['name'] for x in g_list]  for g_list in df['genres']]
df['genres'] = df_dict_to_list

# get list of genres
genre_list = df['genres'].explode().unique()


# plot genre vs no of anime
dict_count = {}

for genre in genre_list:
    df_genre = df[[(genre in g_list) for g_list in df['genres']]]
    dict_count[genre] = len(df_genre.index)

dict_count = dict(sorted(dict_count.items(), key=lambda item: item[1]))

ax = plt.subplot(111)
plt.figure(figsize=(15,7.5))
plt.bar(range(len(dict_count)), list(dict_count.values()), align='center')
plt.xlabel('Genres', fontsize=18)
plt.ylabel('No of Anime', fontsize=18)
plt.xticks(range(len(dict_count)), list(dict_count.keys()), rotation=-45, ha='left')
plt.title('No of Anime vs Genre', fontsize=22)
plt.subplots_adjust(bottom=0.2)
plt.savefig(OUT_DIR+'most_common_genre.jpg')
plt.clf()


# plot genre vs avg-no-users
dict_watch_count = {}

for genre in genre_list:
    df_genre = df[[(genre in g_list) for g_list in df['genres']]]
    mean_no = df_genre['num_list_users'].mean()
    mean_no = mean_no.sum(axis=0)
    dict_watch_count[genre] = mean_no

dict_watch_count = dict(sorted(dict_watch_count.items(), key=lambda item: item[1]))

ax = plt.subplot(111)
plt.figure(figsize=(15,7.5))
plt.bar(range(len(dict_watch_count)), list(dict_watch_count.values()), align='center')
plt.xlabel('Genres', fontsize=18)
plt.ylabel('Average No of Viewers', fontsize=18)
plt.xticks(range(len(dict_watch_count)), list(dict_watch_count.keys()), rotation=-45, ha='left')
plt.title('No of Viewers vs Genre', fontsize=22)
plt.subplots_adjust(bottom=0.2)
plt.savefig(OUT_DIR+'most_watched_genre.jpg')
plt.clf()


# get overlapping plots
combined_df = pd.DataFrame(columns=['genre', 'count', 'viewers'])
for genre in genre_list:
    combined_df.loc[len(combined_df.index)+1] = [genre, dict_count[genre], dict_watch_count[genre]]

fig, ax = plt.subplots(figsize=(15,7.5)) # Create the figure and axes object
# plt.figure(figsize=(25,10))
ax = combined_df.plot(x = 'genre', y = 'viewers', ax = ax, color='#92dff3', kind='bar')
ax2 = combined_df.plot(x = 'genre', y = 'count', ax=ax, color='orange', secondary_y=True) 
ax.set_xticks(range(len(combined_df.index)))
ax.set_xticklabels(list(combined_df['genre']), rotation=-45, ha='left')
ax.set_xlabel('Genres', fontsize=18)
ax.set_ylabel('Average No of Viewers', fontsize=18, color='#0c71e0')
ax2.set_ylabel('Number of Anime', fontsize=18, color='orange')
plt.title('Number of Anime comparison with Viewers for Genres', fontsize=22)
plt.subplots_adjust(bottom=0.2)
fig = plt.gcf()
fig.savefig(OUT_DIR+'genre_popularity_vs_number.jpg')