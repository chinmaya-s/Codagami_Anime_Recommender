import requests
import time
import json

BASE_URL = 'https://api.myanimelist.net/v2/anime/'
# auth_url = 'https://myanimelist.net/v1/oauth2/token'
fields = '?fields=id,title,main_picture,alternative_titles,start_date,end_date,synopsis,mean,rank,popularity,num_list_users,num_scoring_users,nsfw,created_at,updated_at,media_type,status,genres,my_list_status,num_episodes,start_season,broadcast,source,average_episode_duration,rating,pictures,background,related_anime,related_manga,recommendations,studios,statistics'
headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjI1N2I0MTJhYTAwMjlhNzQxZjUxYjVhMDcwM2MxYjUzZTJhNDg1YTVlYjIxZmI3ODY5M2MyNWI0MDFmMDFlMmIxMTQzNTAyOTlmN2Y2OTBkIn0.eyJhdWQiOiIwZWEwNzI0NzkxYjA3ZDVjNWYzNzVhOWJiYjE3YjcxNiIsImp0aSI6IjI1N2I0MTJhYTAwMjlhNzQxZjUxYjVhMDcwM2MxYjUzZTJhNDg1YTVlYjIxZmI3ODY5M2MyNWI0MDFmMDFlMmIxMTQzNTAyOTlmN2Y2OTBkIiwiaWF0IjoxNjM2NzM2MjA0LCJuYmYiOjE2MzY3MzYyMDQsImV4cCI6MTYzOTMyODIwNCwic3ViIjoiMTQwMzQwMTQiLCJzY29wZXMiOltdfQ.ViNlAY_w8M6SQjiB7KFUbLytwWkwCjd776dmu6p7gVVOfAZZbgoYYX-Xrer1Xk815QBt2-48SxOCeJAlsnLRhO5BfW27hN2E6u5yVaBiTbdRPiPETp_EhOZNwUJRYx7qjvyPdCS3YjjLASb8A52hGgWpfRLCpWeihzZTiSymNs1V0GrGzVeeb-f79WuNCUnyI3vTYiFd80SnhrYnfJMKYcVof1DyKmUIvKX3AsNiq8NjDi30-Z0dn_H5kocO3BJTHt2xhH-dXe2fqGNmiRLF434fOXTsOx6M-ha7h2DPOxQKwnUS9gjT2ACE-XyGNGYnU9xiiO9o7r1SGYfF-cY6tg"}
# response = requests.get(BASE_URL+'1'+fields, headers = headers)

# Read token from auth response
# response_json = response.json()


# print(response_json)
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
    url = BASE_URL+id+fields
    # time.sleep(4)
    response = requests.get(url, headers=headers)
    response_json = response.json()
    anime_list.append(response_json)

anime_list1 = []
# f = open('anime_list.json', 'w')
# json_string = json.dumps(anime_list)
# print(type(json_string))
# print(json_string)

with open('anime_list.json', 'a', encoding='utf-8') as f:
    f.write("{")
    for anime in anime_list:
        # f.write(json.dumps(anime))
        # f.write(',')
        json.dump(anime,f,ensure_ascii=False,indent=4)
        f.write("\n,\n")
    f.write('}')
# for anime in anime_list:    
#     json_obj = json.dumps(anime)
#     anime_list1.append(json_obj)
#     # print(f"type = {type(json_obj)}---\njson--{json_obj}")
# # print(type(anime_list))
# print(anime_list1)