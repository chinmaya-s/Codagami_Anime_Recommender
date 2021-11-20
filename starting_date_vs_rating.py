import pandas as pd
import json
from pathlib import Path

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
df = df[['id', 'start_date', 'media_type', 'mean']]
df = df.dropna(subset=['id', 'mean'])
df['start_date'] = pd.to_datetime(df['start_date'])

# considering only tv, ona and music
df1 = df[((df['media_type'] == 'tv') | (df['media_type']
         == 'ona') | (df['media_type'] == 'movie'))]
df1 = df1[['start_date', 'mean']]
df1 = df1.groupby(df1['start_date'].dt.to_period('Y'))['mean'].agg('mean')
fig = df1.plot(ylabel='rating', xlabel='Start Date',
               title='Rating trends against the starting date for movie, tv and ona type animes').get_figure()
fig.savefig('outputs/choosy-2.jpeg')

# considering all the media types
df2 = df[['start_date', 'mean']]
df2 = df2.groupby(df2['start_date'].dt.to_period('Y'))['mean'].agg('mean')
fig2 = df2.plot(ylabel='Rating', xlabel='Start Date',
                title='Rating trends against the starting date of animes').get_figure()
fig2.savefig('outputs/all-2.jpeg')
