from flask import Flask
app=Flask(__name__)


@app.route("/")
def hello():
    return "please like this  video"




app.run(debug=True)