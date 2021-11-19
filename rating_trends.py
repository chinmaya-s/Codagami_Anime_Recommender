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
df.dropna(subset=['rating'], inplace=True)
df['start_date']= pd.to_datetime(df['start_date'])


# %%
df1 = df.groupby(['start_date', 'rating'], as_index=False)['id'].count()
df1.rename({'id': 'anime_count'}, axis=1, inplace=True)
df1 = df1.pivot(index='start_date', columns='rating', values='anime_count')


# %%
# Grouping by year to make the plot smoother
plot = df1.groupby([(df1.index.year)]).sum().plot(title='Number of anime started by rating by year')
savePlot(plot, 'rating_num_anime_vs_year')


# %%
df2 = df.groupby(['rating'])['popularity'].mean()
savePlot(df2.plot(kind='bar', title = 'Mean popularity by Age Rating'), 'rating_vs_popularity')


# %%
def generateHistogram(field, title):
    df2 = df.groupby(['rating'])[field].mean()
    plot = df2.plot(kind='bar', title = title + ' by Age Rating', legend=False)
    savePlot(plot, 'rating_vs_' + field)


# %%
df3 = df.groupby(['rating'])['id'].count()
savePlot(df3.plot(kind='bar', title = 'Num anime by Age Rating'), 'rating_count')


# %%
generateHistogram('num_list_users', 'Number of Listed Users')

# %%
generateHistogram('num_episodes', 'Avg Number of Episodes')

# %%
df['average_episode_duration'] /= 60
generateHistogram('average_episode_duration', 'Avg Episode Duration')

# %%
generateHistogram('mean', 'Avg Score')

# %%
generateHistogram('rank', 'Avg Rank')

# %%
# plot_fields = ['mean', 'rank', 'num_list_users', 'num_episodes','average_episode_duration']
# for field in plot_fields:
    # generateHistogram(field)





