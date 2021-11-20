import pandas as pd
import json
from pathlib import Path
import matplotlib.pyplot as plt
import math 
from scipy.stats import pearsonr
import numpy as np

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

# print(pd.concat(df_list, axis=1))
df = df[df['error'] != 'not_found']

df = df[['id', 'title', 'mean', 'related_anime', 'rank', 'popularity', 'num_list_users']]

df = df[df['related_anime'].str.len() != 0]
df_score = df[df['mean'].notna()]

pd.options.mode.chained_assignment = None 
related_mean = []
related_num_users = []
for index, row in df_score.iterrows():
    related_anime = row['related_anime']
    count = 0
    run_sum = 0
    run_num_users = 0
    for anime in related_anime:
        # print(anime['node']['id'])
        anime_row = df_score[df_score['id'] == anime['node']['id']]
        if anime_row.empty:
            continue
        count = count+1
        run_sum = run_sum + anime_row['mean'].iloc[0]
        run_num_users = run_num_users + anime_row['num_list_users'].iloc[0]
    
    if count == 0:
        count = 1
        run_sum = row['mean']
        run_num_users = row['num_list_users']
    
    related_mean = related_mean + [run_sum/count]
    related_num_users = related_num_users + [run_num_users/count]
    # df_score.at[index, 'related_mean'] = run_sum/count
    # df_score.at[index, 'related_num_users'] = run_num_users/count
    # df_score['related_mean'][index] = run_sum/count
    # df_score['related_num_users'][index] = run_num_users/count
    
    # break
df_score['related_mean'] = related_mean
df_score['related_num_users'] = related_num_users


# score_relation = pearsonr(df_score['mean'], df_score['related_mean'])
# score_relation
mean_arr = np.array(df_score['mean'])
related_mean_arr = np.array(df_score['related_mean'])

score_relation = pearsonr(mean_arr[:4000], related_mean_arr[:4000])
print("Score correlations Pearson")
print(score_relation)
score_relation = pearsonr(mean_arr[4001:8000], related_mean_arr[4001:8000])
print(score_relation)

print("Number of users relation Pearson")
num_users_relation = pearsonr(df_score['num_list_users'][:4000], df_score['related_num_users'][:4000])
print(num_users_relation)
num_users_relation = pearsonr(df_score['num_list_users'][4001:8000], df_score['related_num_users'][4001:8000])
print(num_users_relation)