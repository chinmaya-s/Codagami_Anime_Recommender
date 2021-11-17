import pandas as pd
import numpy as np
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
df.dropna(subset=['genres', 'num_list_users','popularity','start_date'], inplace=True)

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
print(dict_count)

ax = plt.subplot(111)
plt.figure(figsize=(25,10))
plt.bar(range(len(dict_count)), list(dict_count.values()), align='center')
plt.xlabel('Genres')
plt.ylabel('No of Anime')
plt.xticks(range(len(dict_count)), list(dict_count.keys()), rotation=-45, ha='left')
plt.title('No of Anime vs Genre')
plt.subplots_adjust(bottom=0.2)
plt.savefig(OUT_DIR+'most_common_genre.jpg')