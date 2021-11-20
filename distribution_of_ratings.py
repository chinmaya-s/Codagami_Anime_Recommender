# import pandas as pd
# import json
# from pathlib import Path
# import matplotlib.pyplot as plt
# import math 

# # pathlist = Path('data').rglob('*.json')
# # df_list = []
# # for path in pathlist:
#     # because path is object not string
# # path_in_str = str(path)
# json_file = open('data/user_data.json')
# data = json.load(json_file)
# df = pd.DataFrame.from_dict(data, orient='index')
# # df_list.append(df)

# print(df)


import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt
import itertools

path_in_str = 'data/user_data.json'
json_file = open(path_in_str)
data = json.load(json_file)
df = pd.DataFrame.from_dict(data, orient='index')
df = df[df['error'].isna()]

df['user'] = df.index
df.reset_index(inplace=True)
df['user_id'] = df.index

def melt_series(s):
    lengths = s.str.len().values
    flat = [i for i in itertools.chain.from_iterable(s.values.tolist())]
    idx = np.repeat(s.index.values, lengths)
    return pd.Series(flat, idx, name=s.name)


df1 = melt_series(df.data).to_frame().join(df.drop('data', 1))

df1['anime_id'] = df1['data'].apply(lambda x : x['node']['id'])
df1['status'] = df1['data'].apply(lambda x : x['list_status']['status'])
df1['score'] = df1['data'].apply(lambda x : x['list_status']['score'])
df1['is_rewatching'] = df1['data'].apply(lambda x : x['list_status']['is_rewatching'])

df1 = df1[['user', 'user_id', 'anime_id', 'status', 'score', 'is_rewatching']]
df1 = df1.rename({'score': 'user_score'}, axis=1)

# print(df1)

num_scorers = []

for i in range(1, 11):
    df_temp = df1[df1['user_score'] == i]
    num_scorers.append(len(df_temp.index))

print(num_scorers)

fig = plt.figure()
 
# creating the bar plot
plt.bar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], num_scorers)
 
plt.xlabel("Rating")
plt.ylabel("No. of ratings")
plt.title("Distribution of ratings")

fig.savefig('outputs/distribution_of_scores.jpg')