import requests
import time
import json

BASE_URL = 'https://api.myanimelist.net/v2/anime/'
fields = '?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,recommendations,studios,statistics'
headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjI1N2I0MTJhYTAwMjlhNzQxZjUxYjVhMDcwM2MxYjUzZTJhNDg1YTVlYjIxZmI3ODY5M2MyNWI0MDFmMDFlMmIxMTQzNTAyOTlmN2Y2OTBkIn0.eyJhdWQiOiIwZWEwNzI0NzkxYjA3ZDVjNWYzNzVhOWJiYjE3YjcxNiIsImp0aSI6IjI1N2I0MTJhYTAwMjlhNzQxZjUxYjVhMDcwM2MxYjUzZTJhNDg1YTVlYjIxZmI3ODY5M2MyNWI0MDFmMDFlMmIxMTQzNTAyOTlmN2Y2OTBkIiwiaWF0IjoxNjM2NzM2MjA0LCJuYmYiOjE2MzY3MzYyMDQsImV4cCI6MTYzOTMyODIwNCwic3ViIjoiMTQwMzQwMTQiLCJzY29wZXMiOltdfQ.ViNlAY_w8M6SQjiB7KFUbLytwWkwCjd776dmu6p7gVVOfAZZbgoYYX-Xrer1Xk815QBt2-48SxOCeJAlsnLRhO5BfW27hN2E6u5yVaBiTbdRPiPETp_EhOZNwUJRYx7qjvyPdCS3YjjLASb8A52hGgWpfRLCpWeihzZTiSymNs1V0GrGzVeeb-f79WuNCUnyI3vTYiFd80SnhrYnfJMKYcVof1DyKmUIvKX3AsNiq8NjDi30-Z0dn_H5kocO3BJTHt2xhH-dXe2fqGNmiRLF434fOXTsOx6M-ha7h2DPOxQKwnUS9gjT2ACE-XyGNGYnU9xiiO9o7r1SGYfF-cY6tg"}

lines = []
with open('data/anime_ids.txt') as f:
    lines = f.readlines()

anime_dict = {}
# for i in range(4): # change 4 to 23147 while collecting data
for id in lines:
    url = BASE_URL+id.strip()+fields
    response = requests.get(url, headers=headers)
    response_json = response.json()
    anime_dict[int(id)] = response_json

try:
    geeky_file = open('anime_list_final.json', 'w')
    json_str = json.dump(anime_dict, geeky_file, ensure_ascii=False, indent=4)
    geeky_file.close()
  
except:
    print("Unable to write to file")
# print(anime_dict)
# anime_list.append(response_json)
