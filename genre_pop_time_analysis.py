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

df = df[['genres', 'num_list_users', 'start_date']]
df.dropna(inplace=True)

# change genres column and start_date column
df_dict_to_list = [[x['name'] for x in g_list]  for g_list in df['genres']]
df['genres'] = df_dict_to_list
df['start_date'] = pd.to_datetime(df['start_date'])
df['start_date'] = df['start_date'].dt.year
df.dropna(inplace=True)
df['start_date'] = df['start_date'].astype(int)
df = df[df['start_date'] < 2022]
df['start_date'] = (df['start_date']//5)*5

# get list of genres
genre_list = df['genres'].explode().unique()
x = df['start_date'].tolist()
ax = plt.gca()

# get the plot 
for genre in genre_list:
    df_genre = df[[(genre in g_list) for g_list in df['genres']]]
    df_genre_group = df_genre.groupby('start_date').agg({'num_list_users': 'mean'}).reset_index()
    df_genre_group.plot( x='start_date' , y='num_list_users', rot=-45, ax=ax, figsize=(25,10))

plt.legend(genre_list, bbox_to_anchor=(1,1.1))
plt.xlabel('Start Year')
plt.ylabel('Average No of Viewers')
plt.title('Popularity Time Analysis of Genres')
plt.subplots_adjust(bottom=0.15, right=0.85)
fig = plt.gcf()
fig.set_size_inches(20, 10)
fig.savefig(OUT_DIR+'genre_popularity_time_analysis.jpg')

