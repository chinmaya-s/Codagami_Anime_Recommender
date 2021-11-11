import requests 
import json
import time

base_url = 'https://api.jikan.moe/v3/anime/'

lines = []
with open('anime_ids.txt') as f:
    lines = f.readlines()

anime_list = []
# response = requests.get(base_url+'6')
# response_json = response.json()
# anime_list = [response_json]
# Line 11574- end of anime id or 23147

for i in range(4): # change 4 to 23147 while collecting data
    id = lines[i]
    # print(base_url+id)
    url = base_url+id
    time.sleep(4)
    response = requests.get(url)
    response_json = response.json()
    anime_list.append(response_json)


f = open('anime_list.json', 'w')
json.dump(anime_list, f)

print(anime_list)
