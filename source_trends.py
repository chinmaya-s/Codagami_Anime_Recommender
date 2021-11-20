# %%
import pandas as pd
import json
import matplotlib as plt


# %%
def savePlot(plot, name):
    fig = plot.get_figure()
    fig.savefig("outputs/" + name + '.jpeg')


# %%
path_in_str = 'data/anime_list_final_231.json'
json_file = open(path_in_str)
data = json.load(json_file)
df = pd.DataFrame.from_dict(data, orient='index')
df = df[df['error'] != 'not_found']
df.dropna(subset=['source'], inplace=True)
df['start_date']= pd.to_datetime(df['start_date'])
df = df[df['start_date'].dt.year < 2022]

# %%
df1 = df.groupby(['start_date', 'source'], as_index=False)['id'].count()
df1.rename({'id': 'anime_count'}, axis=1, inplace=True)
df1 = df1.pivot(index='start_date', columns='source', values='anime_count')
df1 = df1[['game',
       'light_novel', 'manga', 'music', 'novel', 'original', 'other', 'visual_novel']]
# df1.columns
df1.sum(axis=0, skipna=True)


# %%
# Grouping by year to make the plot smoother
plot = df1.groupby([(df1.index.year)]).sum().plot(title='Year-wise number of anime produced by source', ylabel="Number of anime", xlabel="Year", figsize=(10,6))
savePlot(plot, 'source_num_anime_vs_year')


# %%
df2 = df.groupby(['source'])['popularity'].mean()
savePlot(df2.plot(kind='bar', title = 'Mean popularity by source'), 'source_vs_popularity')


# %%
def generateHistogram(field):
    df2 = df.groupby(['source'])[field].mean()
    savePlot(df2.plot(kind='bar', title = 'Mean ' + field + ' by source'), 'source_vs_' + field)


# %%
df3 = df.groupby(['source'])['id'].count()
savePlot(df3.plot(kind='bar', title = 'Num anime by source'), 'source_count')


# %%
# plot_fields = ['mean', 'rank', 'num_list_users', 'num_episodes','average_episode_duration']
# for field in plot_fields:
#     generateHistogram(field)




df
df_rank = df.groupby(['source'])['rank'].mean()
df_pop = df.groupby(['source'])['popularity'].mean()
df_pop.index
frame={'rank': df_rank, 'popularity':df_pop, 'source':df_pop.index}
df4 = pd.DataFrame(frame)
df4
savePlot(df4.plot(kind='bar', x='source', y=['rank', 'popularity'], figsize=(10,10), ylabel="Value of rank/popularity", xlabel="Source Material"), 'source_vs_rank_and_pop')

