import json

with open("list.json",'r') as files:
    datas = json.load(files)
for data in datas:
    if int(data['id']) == 1202020:
        print(data['name'])
 