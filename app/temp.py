import json

with open("data/ramayan.json","r") as f:
    d = json.load(f)

with open("data/ramayan2.json","w+") as f:
    json.dump(d,f,indent=4)