import flask
app = flask.Flask("")


@app.route("/")
def Home():
    return "<01000110><01110010><01101001><01100100><01100001><01111001>"


@app.route("/<path:Path>")
def File(Path):
    try:
        return flask.send_from_directory("data", Path)
    except Exception as e:
        return f"<01000101><01010010><01010010><01001111><01010010> : {type(e).__name__}"

if __name__=="__main__":
    app.run(host="0.0.0.0",debug=False)

# "/index.json"
# "/ramayan.json"
#app.run(host="0.0.0.0", port=8080)h
