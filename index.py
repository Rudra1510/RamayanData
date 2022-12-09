indexText = """01001001 00100000 01100001 01101101 00100000 01110011 01101111 00100000 01101001 01101110 00100000 01101100 01101111 01110110 01100101 00100000 01110111 01101001 01110100 01101000 00100000 01111001 01101111 01110101 00100000 01000100 01001111 01000010 01010101 01010101 01010101 00101110 00101110 00101110 01011001 01000101 01010011 01010011 00100000 01001001 00100000 01000110 01010010 01000101 01000001 01001011 01001001 01001110 01000111 00100000 01001100 01001111 01010110 01000101 00100000 01011001 01001111 01010101 00100001 00100001 00100000 00111100 00110011 00111100 00110011 00111100 00110011"""
import json
import flask
app = flask.Flask("")

import hashlib
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


@app.route("/")
def Home():
    return indexText


# @app.route("/indexhash")
# def indexHash():
#     return md5("data/assets/books/1.json")
    
# @app.route("increaseindex")
# def 


@app.route("/ramayan-api/<path:Path>")
def File(Path):
    try:
        return flask.send_from_directory("", Path)
    except Exception as e:
        return f"{type(e).__name__}"

@app.route("/ramayan-api/index")
def Index():
    try:
        return flask.send_from_directory("","data/assets/index.json")
    except Exception as e:
        return f"{type(e).__name__}"
    
@app.route("/ramayan-api/chapter/<path:Bkno>/<path:Chno>/<path:Lang>")
def chapter(Bkno,Chno,Lang):
    Chno = int(Chno)
    Bkno = int(Bkno)
    
    with open(f"data/assets/books/{Bkno+1}.json","r") as f:
        d = json.load(f)

    if Lang == "all":
        return d["content"][Chno]

    else:
        Languages = Lang.split("-")
        OutputJSON = {}
        OutputJSON["mainTitle"] = d["content"][Chno]["mainTitle"]
        OutputJSON["content"] = []
        OutputChapters = []
        for i in range(len(d["content"][Chno]["content"])):
            chapter = {}
            chapter["title"] = d["content"][Chno]["content"][i]["title"]
            for l in Languages:
                chapter[l] = d["content"][Chno]["content"][i][l]
            OutputChapters.append(chapter)
        OutputJSON["content"] = OutputChapters

        return OutputJSON
    

# @app.route("/indexx")
# def index():

#     with open("data/assets/index.json","r") as f:
#         d = json.load(f)

    
        
#     for i in range(1,len(d["books"])+1):

#         d["books"][i-1]["subIndex"] = []

#         with open(f"data/assets/books/{str(i)}.json","r") as f:
#             b = json.load(f)

#             for j in range(len(b["content"])):

#                 shlokaTitles = []
#                 for k in b["content"][j]["content"]:
#                     shlokaTitles.append(k["title"])

#                 x= {
#                         "chapterTitle":[b["content"][j]["mainTitle"]][0], 
#                         "chapterIndex":shlokaTitles
#                         }

#                 # d["books"][i-1]["index"][b["content"][j]["mainTitle"]] = shlokaTitles
#                 d["books"][i-1]["subIndex"].append(x)

#     with open("data/assets/index.json","w+") as f:
#         json.dump(d,f,indent=4)


        

#         # i["index"] = 0

    
    

#     return "hey"

    
if __name__=="__main__":
    app.run(port=5051)