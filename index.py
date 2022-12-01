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
    return "<01000110><01110010><01101001><01100100><01100001><01111001>"


@app.route("/indexhash")
def indexHash():
    return md5("data/assets/books/1.json")
    
# @app.route("increaseindex")
# def 


@app.route("/<path:Path>")
def File(Path):
    try:
        return flask.send_from_directory("", Path)
    except Exception as e:
        return f"{type(e).__name__}"
    

@app.route("/main")
def Main():
    try:
        return flask.send_from_directory("","data/assets/index.json")
    except Exception as e:
        return f"{type(e).__name__}"
    
@app.route("/chapter/<path:Bkno>/<path:Chno>/<path:Lang>")
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
    

@app.route("/index")
def index():

    with open("data/assets/index.json","r") as f:
        d = json.load(f)

    
        
    for i in range(1,len(d["books"])+1):

        d["books"][i-1]["subIndex"] = []

        with open(f"data/assets/books/{str(i)}.json","r") as f:
            b = json.load(f)

            for j in range(len(b["content"])):

                shlokaTitles = []
                for k in b["content"][j]["content"]:
                    shlokaTitles.append(k["title"])

                x= {
                        "chapterTitle":[b["content"][j]["mainTitle"]][0], 
                        "chapterIndex":shlokaTitles
                        }

                # d["books"][i-1]["index"][b["content"][j]["mainTitle"]] = shlokaTitles
                d["books"][i-1]["subIndex"].append(x)

    with open("data/assets/index.json","w+") as f:
        json.dump(d,f,indent=4)


        

        # i["index"] = 0

    
    

    return "hey"

    
if __name__=="__main__":
    app.run(port=5051)