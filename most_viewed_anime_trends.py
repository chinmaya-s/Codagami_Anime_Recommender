import pandas as pd
import json
from pathlib import Path
import matplotlib.pyplot as plt

# Code to load data
pathlist = Path('data').rglob('*.json')
df_list = []
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    json_file = open(path_in_str)
    data = json.load(json_file)
    df = pd.DataFrame.from_dict(data, orient='index')
    df_list.append(df)

df = pd.concat(df_list, axis=1)

# Preprocess data
df = df[['id', 'media_type', 'statistics']]
df = df.dropna(subset=['id'])

#########################################################
# This section creates plot on which x-axis is media_type
# and y-axis is the number of animes made of that type
#########################################################
mediaDF = df[['media_type']]
mediaDF['count'] = mediaDF.groupby(
    'media_type')['media_type'].transform('count')
mediaDF.drop_duplicates(inplace=True)
mediaDF.reset_index(inplace=True)
mediaDF = mediaDF[['media_type', 'count']]
mediaDF = mediaDF[~(mediaDF['media_type'] == 'unknown')]

fig = mediaDF.plot(x='media_type', y='count', kind='bar', xlabel='Media Types',
                   ylabel='Number of animes', title='Number of animes produced of each media type').get_figure()
plt.tight_layout()
fig.savefig('outputs/animes_based_on_media_type_trends.jpeg')

#########################################################
# This section creates plot on which x-axis is media_type
# and y-axis is the number of users who watch this type
#########################################################
df = df.dropna(subset=['media_type', 'statistics'])

userDF = pd.DataFrame(columns=['media_type', 'users'])
idxCount = 0
for _, row in df.iterrows():
    userDF.loc[idxCount] = [row['media_type'],
                            row['statistics']['num_list_users']]
    idxCount = idxCount + 1

userDF = userDF.groupby('media_type', as_index=False).agg('sum')
userDF = userDF[~(userDF['media_type'] == 'unknown')]

fig = userDF.plot(x='media_type', y='users', kind='bar', xlabel='Media Types', ylabel='Number of users',
                  title='Number of viewers of animes based on theit media types').get_figure()
plt.tight_layout()
fig.savefig('outputs/media_type_trends_based_on_users.jpeg')
