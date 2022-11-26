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

    
if __name__=="__main__":
    app.run(port=9596)