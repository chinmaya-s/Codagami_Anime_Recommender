import requests
from bs4 import BeautifulSoup


URL = "https://myanimelist.net/info.php?search=%25%25%25&go=relationids&divname=relationGen1"
r = requests.get(URL)
# print(r.content)

soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())

ids=[]

ids_list1 = soup.find_all('td', attrs = { 'class':'td1'}) 
ids_list2 = soup.find_all('td', attrs = {'class': 'td2'})
# print(ids_list)

for id in ids_list1:
    a = id.a
    if(a):
        ids.append(a.text)

for id in ids_list2:
    a = id.a
    if(a):
        ids.append(a.text)

print(len(ids))
sorted(ids)

with open('data/anime_ids.txt', 'w') as f:
    for item in ids:
        f.write("%s\n" % item)