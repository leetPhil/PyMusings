#object and arrays in JSON map to dict and list in Py

import json

jsonobj = json.load(open('sample.json'))

print(jsonobj['people'][1])