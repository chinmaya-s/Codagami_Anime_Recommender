## Output: outputs/num_anime_vs_date.jpeg

# %%
import pandas as pd
import json

# %%
path_in_str = 'data/anime_list_final_231.json'
json_file = open(path_in_str)
data = json.load(json_file)
df = pd.DataFrame.from_dict(data, orient='index')
df = df[df['error'] != 'not_found']

# %%
df['start_date']= pd.to_datetime(df['start_date'])
# df = df[df['start_date'].dt.year < 2022]

# %%
df1 = df.groupby('start_date', as_index=False)['id'].count()

# %%
df1.set_index(['start_date'], inplace=True)

# %%
df1.rename({'id': 'anime_count'}, axis=1, inplace=True)

# %%
# plot = df1.plot()
# Grouping by year to make the plot smoother
plot = df1.groupby([(df1.index.year)]).sum().plot(title='Number of anime started vs year', xlabel='Start Year', ylabel='Anime Count', legend=False)
fig = plot.get_figure()
fig.savefig("outputs/num_anime_vs_year.jpeg", bbox_inches='tight')
