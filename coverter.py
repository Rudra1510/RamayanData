import json

with open("data/assets/books/1Rawx.json","r") as f:
    d = json.load(f)

o = []










for i in d:

    # title = i
    chapterContents = []

    for j in d[i]:

        title = j.lstrip('0')

        english = d[i][j]["eng"]
        sanskrit = d[i][j]["sans"].replace("|| ","||\n")

        z = {
                        "title":title,
                        "english":english,
                        "hindi":"-",
                        "sanskrit":sanskrit,
                        "meanings":"-"
                    }
        chapterContents.append(z)
        

    x= {
            "mainTitle":f"Chapter Title {i.lstrip('0')}",
            "content":chapterContents
        }

    o.append(x)


output = {"content":o}

with open("data/assets/books/1C.json","w+") as f:
    json.dump(output,f,indent=4)