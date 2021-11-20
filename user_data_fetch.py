import requests 
import json
import time

base_url = 'https://api.myanimelist.net/v2/users/'
base_username = 'chinmay453'

lines = []
with open('data/username_list.txt') as f:
    lines = f.readlines()
headers = {"Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjI1N2I0MTJhYTAwMjlhNzQxZjUxYjVhMDcwM2MxYjUzZTJhNDg1YTVlYjIxZmI3ODY5M2MyNWI0MDFmMDFlMmIxMTQzNTAyOTlmN2Y2OTBkIn0.eyJhdWQiOiIwZWEwNzI0NzkxYjA3ZDVjNWYzNzVhOWJiYjE3YjcxNiIsImp0aSI6IjI1N2I0MTJhYTAwMjlhNzQxZjUxYjVhMDcwM2MxYjUzZTJhNDg1YTVlYjIxZmI3ODY5M2MyNWI0MDFmMDFlMmIxMTQzNTAyOTlmN2Y2OTBkIiwiaWF0IjoxNjM2NzM2MjA0LCJuYmYiOjE2MzY3MzYyMDQsImV4cCI6MTYzOTMyODIwNCwic3ViIjoiMTQwMzQwMTQiLCJzY29wZXMiOltdfQ.ViNlAY_w8M6SQjiB7KFUbLytwWkwCjd776dmu6p7gVVOfAZZbgoYYX-Xrer1Xk815QBt2-48SxOCeJAlsnLRhO5BfW27hN2E6u5yVaBiTbdRPiPETp_EhOZNwUJRYx7qjvyPdCS3YjjLASb8A52hGgWpfRLCpWeihzZTiSymNs1V0GrGzVeeb-f79WuNCUnyI3vTYiFd80SnhrYnfJMKYcVof1DyKmUIvKX3AsNiq8NjDi30-Z0dn_H5kocO3BJTHt2xhH-dXe2fqGNmiRLF434fOXTsOx6M-ha7h2DPOxQKwnUS9gjT2ACE-XyGNGYnU9xiiO9o7r1SGYfF-cY6tg"}
fields = "?fields=list_status&limit=1000"

user_data = {}
i = 0
# for i in range(4): # change 4 to 23147 while collecting data
for user in lines:
    url = base_url+user.strip()+"/animelist"+fields
    print(url)
    response = requests.get(url, headers=headers)
    response_json = response.json()
    user_data[user.strip()] = response_json
    # break
    i = i+1
    if i%100 == 0:
        geeky_file = open('user_data'+str(i/100)+'.json', 'w+')
        json_str = json.dump(user_data, geeky_file, ensure_ascii=False, indent=4)
        geeky_file.close()

try:
    geeky_file = open('user_data.json', 'w+')
    json_str = json.dump(user_data, geeky_file, ensure_ascii=False, indent=4)
    geeky_file.close()
  
except:
    print("Unable to write to file")

# response = requests.get(base_url+username+'/friends')
# response_json = response.json()

# username_list = ['chinmay453']

# i = 0

# max_users = 10000

# username_dict = {'chinmay453'}

# while i < min(len(username_list), max_users):
#     username = username_list[i]
#     response = requests.get(base_url+username+'/friends')
#     response_json = response.json()
#     print(i, username)
#     try:
#         for friend in response_json['friends']:
#             new_user = friend['username']
#             if new_user not in username_dict:
#                 username_list.append(new_user)
#                 username_dict.add(new_user)
#     except:
#         time.sleep(4)
#         continue
#     time.sleep(4)
#     i = i+1
#     if i%100 == 0:
#         with open('username_list'+str(i/100)+'.txt', 'w+') as f:
#             for item in username_list:
#                 f.write("%s\n"%item)

# print(username_list)