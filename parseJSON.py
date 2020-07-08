import json

jsonobj = json.load(open('sample.json'))

print(jsonobj['people'][1])