# %%
import pandas as pd
import json
import matplotlib as plt


# %%
def savePlot(plot, name):
    fig = plot.get_figure()
    fig.savefig("outputs/" + name + '.jpeg', bbox_inches='tight')


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
plot = df1.groupby([(df1.index.year)]).sum().plot(title='Number of anime started by year', xlabel='Start Year', ylabel='No of anime started')
savePlot(plot, 'rating_num_anime_vs_year')


# %%
df2 = df.groupby(['rating'])['popularity'].mean()
savePlot(df2.plot(kind='bar', title = 'Mean popularity by Age Rating', xlabel='Age Rating', ylabel='Mean Popularity', legend=False), 'rating_vs_popularity')


# %%
def generateHistogram(field, title, ylabel):
    df2 = df.groupby(['rating'])[field].mean()
    plot = df2.plot(kind='bar', title = title + ' by Age Rating', xlabel='Age Rating', ylabel=ylabel, legend=False)
    savePlot(plot, 'rating_vs_' + field)


# %%
len(df.id.unique())

# %%
df3 = df.groupby(['rating'])['id'].count()
savePlot(df3.plot(kind='bar', title = 'Anime Count by Age Rating', xlabel='Age Rating', ylabel='Anime Count', legend=False), 'rating_count')


# %%
generateHistogram('num_list_users', 'Number of Users', 'No of users')

# %%
generateHistogram('num_episodes', 'Average Number of Episodes', 'Average episode count')

# %%
df['average_episode_duration'] /= 60
generateHistogram('average_episode_duration', 'Average Episode Duration', 'Average episode duration (min)')

# %%
generateHistogram('mean', 'Average Score', 'Average Score')

# %%
generateHistogram('rank', 'Average Rank', 'Average Rank')

# %%
# plot_fields = ['mean', 'rank', 'num_list_users', 'num_episodes','average_episode_duration']
# for field in plot_fields:
    # generateHistogram(field)





