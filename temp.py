import json

with open("data/assets/books/1.json","r") as f:
    d = json.load(f)["content"]
    
print(len([i for i in d]))