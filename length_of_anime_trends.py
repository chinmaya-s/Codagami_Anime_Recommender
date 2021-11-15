import pandas as pd
import json
from pathlib import Path
import math 

pathlist = Path('data').rglob('*.json')
df_list = []
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    json_file = open(path_in_str)
    data = json.load(json_file)
    df = pd.DataFrame.from_dict(data, orient='index')
    df_list.append(df)
    #  print(path_in_str)

# print(pd.concat(df_list, axis=1))
df = df[df['error'] != 'not_found']
# print(df)
num_episodes = df['num_episodes'].unique()

episode_count_range = [0, 11, 21, 31, 51, 101, 201, 501, 1001]
episode_count_range_high = [10, 20, 30, 50, 100, 200, 500]

df_score = df[df['mean'].notna()]

excluded_media_types = ['ova', 'special', 'music']

df_score_trim = df_score

for type in excluded_media_types:
    df_score_trim = df_score_trim[df_score_trim['media_type'] != type]

length_trends = pd.DataFrame(columns=['Episode count', 'Number of anime', 'Average score', 'Average no. of users'])
length_trends_total = pd.DataFrame(columns=['Episode count', 'Number of anime', 'Average score', 'Average no. of users'])

def find_trends(min_ep, max_ep, row_name):

    # Trimmed data
    df_curr = df_score_trim

    df_curr = df_curr[df_curr['num_episodes'] >= min_ep]
    df_curr = df_curr[df_curr['num_episodes'] <= max_ep]

    num_anime = len(df_curr.index)
    avg_score = df_curr['mean'].mean()
    avg_num_users = df_curr['num_list_users'].mean()
    print(num_anime, avg_score, avg_num_users)

    length_trends.loc[len(length_trends.index)] = [row_name, num_anime, avg_score, avg_num_users]

    # Untrimmed data
    df_curr = df_score

    df_curr = df_curr[df_curr['num_episodes'] >= min_ep]
    df_curr = df_curr[df_curr['num_episodes'] <= max_ep]

    num_anime = len(df_curr.index)
    avg_score = df_curr['mean'].mean()
    avg_num_users = df_curr['num_list_users'].mean()
    # print(num_anime, avg_score, avg_num_users)

    length_trends_total.loc[len(length_trends_total.index)] = [row_name, num_anime, avg_score, avg_num_users]

    return

find_trends(0, 9, '0-9')
find_trends(10, 19, '10-19')
find_trends(20, 29, '20-29')
find_trends(30, 49, '30-49')
find_trends(50, 99, '50-99')
find_trends(100, 199, '100-199')
find_trends(200, 499, '200-499')
find_trends(500, 999, '500-999')
find_trends(1000, math.inf, '1000+')

length_trends.to_csv('outputs/length-of-anime-trends.csv', index = False)
length_trends_total.to_csv('outputs/length-of-anime-trends-untrimmed.csv', index = False)