from numpy.core.fromnumeric import mean
import pandas as pd
import json
import matplotlib.pyplot as plt

INP_DIR = 'data/'
OUT_DIR = 'outputs/'

# Genre analysis- most watched (avg no. of users), related (later), most common (no. of anime), popularity time analysis

# get data from json in a dataframe
path_in_str = 'anime_list_final_231.json'
json_file = open(INP_DIR+path_in_str)
data = json.load(json_file)
df = pd.DataFrame.from_dict(data, orient='index')
# print(df.columns)

df = df[['genres', 'num_list_users','popularity','start_date','end_date']]
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
plt.figure(figsize=(25,10))
plt.bar(range(len(dict_count)), list(dict_count.values()), align='center')
plt.xlabel('Genres')
plt.ylabel('No of Anime')
plt.xticks(range(len(dict_count)), list(dict_count.keys()), rotation=-45, ha='left')
plt.title('No of Anime vs Genre')
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
plt.figure(figsize=(25,10))
plt.bar(range(len(dict_watch_count)), list(dict_watch_count.values()), align='center')
plt.xlabel('Genres')
plt.ylabel('Average No of Viewers')
plt.xticks(range(len(dict_watch_count)), list(dict_watch_count.keys()), rotation=-45, ha='left')
plt.title('No of Viewers vs Genre')
plt.subplots_adjust(bottom=0.2)
plt.savefig(OUT_DIR+'most_watched_genre.jpg')
plt.clf()