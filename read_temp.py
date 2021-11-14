# importing the module
import json
  
# reading the data from the file
with open('anime_list1.json') as f:
    data = f.read()
  
js = json.loads(data)
  
print("Data type after reconstruction : ", type(js))
print(js)