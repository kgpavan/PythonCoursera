import json
import urllib.request, urllib.parse, urllib.error


# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Chuck"
#   }
# ]'''

address = input()
uh = urllib.request.urlopen(address)
data = uh.read()
info = json.loads(data)
#print(info['comments'])
sumc = 0
for li in info['comments']:
    c = int(li['count'])
    sumc = sumc + c
print(sumc)
# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])
