# %%
import pandas as pd
import numpy as np
import json
import itertools


def load_recommender_data(path_in_str):
    json_file = open(path_in_str)
    data = json.load(json_file)
    df = pd.DataFrame.from_dict(data, orient='index')
    df = df[df['error'].isna()]

    # %%
    df['user'] = df.index
    df.reset_index(inplace=True)
    df['user_id'] = df.index

    # %%
    def melt_series(s):
        lengths = s.str.len().values
        flat = [i for i in itertools.chain.from_iterable(s.values.tolist())]
        idx = np.repeat(s.index.values, lengths)
        return pd.Series(flat, idx, name=s.name)


    user_df = melt_series(df.data).to_frame().join(df.drop('data', 1))

    # %%
    user_df['anime_id'] = user_df['data'].apply(lambda x : x['node']['id'])
    user_df['status'] = user_df['data'].apply(lambda x : x['list_status']['status'])
    user_df['score'] = user_df['data'].apply(lambda x : x['list_status']['score'])
    user_df['is_rewatching'] = user_df['data'].apply(lambda x : x['list_status']['is_rewatching'])


    # %%
    user_df = user_df[['user', 'user_id', 'anime_id', 'status', 'score', 'is_rewatching']]
    user_df = user_df.rename({'score': 'user_score'}, axis=1)

    # %%
    path_in_str = 'data/anime_list_final_231.json'
    json_file = open(path_in_str)
    data = json.load(json_file)
    anime_df_raw = pd.DataFrame.from_dict(data, orient='index')
    anime_df_raw = anime_df_raw[anime_df_raw['error'] != 'not_found']
    anime_df = anime_df_raw[['id', 'title', 'mean', 'genres', 'statistics', 'num_episodes']]
    anime_df = anime_df.dropna()

    # %%
    anime_df['genres_name'] = anime_df['genres'].apply(lambda x : [a['name'] for a in x])
    anime_df['genres_id'] = anime_df['genres'].apply(lambda x : [a['id'] for a in x])

    # %%
    anime_df['watching'] = anime_df['statistics'].apply(lambda x : x['status']['watching'])
    anime_df['num_list_users'] = anime_df['statistics'].apply(lambda x : x['num_list_users'])
    anime_df['completed'] = anime_df['statistics'].apply(lambda x : x['status']['completed'])
    anime_df['plan_to_watch'] = anime_df['statistics'].apply(lambda x : x['status']['plan_to_watch'])
    anime_df['dropped'] = anime_df['statistics'].apply(lambda x : x['status']['dropped'])
    anime_df['on_hold'] = anime_df['statistics'].apply(lambda x : x['status']['on_hold'])

    # %%
    anime_df.drop(['genres', 'statistics'], axis=1, inplace=True)

    # %%
    anime_df.rename({'id': 'anime_id'}, axis=1, inplace=True)



    # %%
    df_merge_raw = pd.merge(anime_df, user_df, on = 'anime_id')

    # %%
    df_merge = df_merge_raw[['anime_id', 'title', 'genres_name', 'num_episodes', 'mean', 'num_list_users', 'user_id', 'user_score']]

    # %%
    df_merge.rename({'title': 'name', 'genres_name': 'genre', 'num_episodes': 'episodes', 'mean': 'rating_x', 'num_list_users': 'members', 'user_score': 'rating_y'}, axis=1, inplace= True)

    # %%
    df_merge['rating_x'] = df_merge['rating_x'].astype(int)
    df_merge['rating_x'] = df_merge['rating_x'].round()

    return df_merge, anime_df, user_df


def main():
    path_in_str = 'user_data1.0.json'
    load_recommender_data(path_in_str)
