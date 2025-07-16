from flask import Flask
app=Flask(__name__)


@app.route("/")
def hello():
    return "please like this  video"


@app.route("/siddhi")
def siddhi():
    return"hello siddhi"


@app.route("/<name>/")
def helloname(name):
    return "hello"+ name


@app.route("/<int:date>")
def hellod(date):
    return "date= %d" % date

@app.route("/<float:date>")
def hellom(date):
    return "date= %f" % date

app.run(debug=True)