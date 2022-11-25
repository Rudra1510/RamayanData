import flask
app = flask.Flask("")


@app.route("/")
def Home():
    return "<01000110><01110010><01101001><01100100><01100001><01111001>"


@app.route("/<path:Path>")
def File(Path):
    try:
        return flask.send_from_directory("", Path)
    except Exception as e:
        return f"{type(e).__name__}"

    
if __name__=="__main__":
    app.run()