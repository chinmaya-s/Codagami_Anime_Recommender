import requests 
import json
import time

base_url = 'https://api.jikan.moe/v3/user/'
base_username = 'chinmay453'

# response = requests.get(base_url+username+'/friends')
# response_json = response.json()

username_list = ['chinmay453']

i = 0

max_users = 10000

username_dict = {'chinmay453'}

while i < min(len(username_list), max_users):
    username = username_list[i]
    response = requests.get(base_url+username+'/friends')
    response_json = response.json()
    print(i, username)
    try:
        for friend in response_json['friends']:
            new_user = friend['username']
            if new_user not in username_dict:
                username_list.append(new_user)
                username_dict.add(new_user)
    except:
        time.sleep(4)
        continue
    time.sleep(4)
    i = i+1
    if i%100 == 0:
        with open('username_list'+str(i/100)+'.txt', 'w+') as f:
            for item in username_list:
                f.write("%s\n"%item)

print(username_list)