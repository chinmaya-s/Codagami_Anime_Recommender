## List of outputs
## outputs/rating_count.jpeg,  outputs/rating_num_anime_vs_year.jpeg, 
# outputs/rating_vs_average_episode_duration.jpeg, 
# outputs/rating_vs_mean.jpeg, outputs/rating_vs_num_episodes.jpeg, 
# outputs/rating_vs_num_list_users.jpeg,
# outputs/rating_vs_popularity.jpeg, outputs/rating_vs_rank.jpeg

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
savePlot(df2.plot(kind='bar', title = 'Mean popularity by rating'), 'rating_vs_popularity')

# %%
def generateHistogram(field):
    df2 = df.groupby(['rating'])[field].mean()
    savePlot(df2.plot(kind='bar', title = 'Mean ' + field + ' by rating'), 'rating_vs_' + field)

# %%
df3 = df.groupby(['rating'])['id'].count()
savePlot(df3.plot(kind='bar', title = 'Num anime by rating'), 'rating_count')

# %%
plot_fields = ['mean', 'rank', 'num_list_users', 'num_episodes','average_episode_duration']
for field in plot_fields:
    generateHistogram(field)


