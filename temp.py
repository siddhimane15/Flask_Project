from flask import Flask,render_template
app=Flask(__name__)


@app.route("/")
def hello():
    return "<html><body><h1>Please like this video,Thank You!!!</h1></body></html>"
    return render_template("index.html")



app.run(debug=True)