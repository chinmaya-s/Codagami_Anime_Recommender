import pandas as pd
import json
from pathlib import Path

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
df = df[['id', 'start_date', 'media_type', 'mean']]
df = df.dropna(subset=['id', 'mean'])
df['start_date'] = pd.to_datetime(df['start_date'])

# considering only tv, ona and music
df1 = df[((df['media_type'] == 'tv') | (df['media_type']
         == 'ona') | (df['media_type'] == 'music'))]
df1 = df1[['start_date', 'mean']]
df1 = df1.groupby(df1['start_date'].dt.to_period('Q'))['mean'].agg('mean')
fig = df1.plot().get_figure()
fig.savefig('choosy-2.jpeg')

# considering all the media types
df2 = df[['start_date', 'mean']]
df2 = df2.groupby(df2['start_date'].dt.to_period('Q'))['mean'].agg('mean')
print(df2)
fig2 = df2.plot().get_figure()
fig2.savefig('all-2.jpeg')
