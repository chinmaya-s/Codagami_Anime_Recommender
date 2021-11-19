# %%
import pandas as pd
import json
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib
import numpy as np


# %%
path_in_str = 'data/anime_list_final_231.json'
json_file = open(path_in_str)
data = json.load(json_file)
df = pd.DataFrame.from_dict(data, orient='index')


# %%
df = df[['rank', 'popularity']]
correalation = df['rank'].corr(df['popularity'], method='pearson')
print(f"correalation = {correalation}")
df.cov()


# %%
df = df.dropna(subset=['rank', 'popularity'])
df['popularity'] = df['popularity'].astype(int)
df['rank'] = df['rank'].astype(int)
df = df[df['rank'] > 0]


# %%
dfc = df.groupby(['rank']).count()
# dfc.describe()
dfc = dfc[dfc['popularity'] == 1]
valid_ranks = dfc.index.to_list()
df = df[df['rank'].isin(valid_ranks)]
df = df.sort_values(by=['rank'])


# %%
# df2[df2['rank'] < 100].plot()
df2 = df.copy()
fig = df2[df2['rank'] < 100].plot(x='rank', y='popularity').get_figure()
fig.savefig("outputs/rank_vs_popularity_first100.jpg")


# %%
interval = 200
df_grouped = df2.groupby(pd.cut(df2["rank"], np.arange(1, 17314+interval, interval))).mean()
fig = df_grouped.plot(y='popularity', x='rank').get_figure()
fig.savefig("outputs/rank_vs_popularity.jpg")

# %%
df1 = df.copy()
def mod_of_vals(row):
    return abs(row['rank'] - row['popularity'])
df1['diff'] = df1.apply(lambda row: mod_of_vals(row), axis=1)
df1.describe()
# df1

# %%
df3 = df.copy()
df3 = df3[df3['rank'] <= 100]
def mod_of_vals(row):
    return abs(row['rank'] - row['popularity'])
df3['diff'] = df3.apply(lambda row: mod_of_vals(row), axis=1)
df3.describe()

# %%
df4 = df.copy()
df4 = df4[df4['popularity'] <= 100]
def mod_of_vals(row):
    return abs(row['rank'] - row['popularity'])
df4['diff'] = df4.apply(lambda row: mod_of_vals(row), axis=1)
df4.describe()


