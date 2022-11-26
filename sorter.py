import json
with open("data/assets/books/1Raw.json","r") as f:
    d = json.load(f)

a = {}

for i in d:
    a[i.zfill(3)] = d[i]
    # del d[i]

b= {}
for i in a:
    b[i]={}
    for j in a[i]:
        b[i][j.zfill(3)] = a[i][j]
        # del a[i][j]


with open("data/assets/books/1Rawx.json","w+") as f:
    json.dump(b,f,sort_keys=True,indent=4)


