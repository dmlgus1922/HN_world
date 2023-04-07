import json

with open('sample.json') as f:
    js = json.load(f)

print(js[0]['user_id'])