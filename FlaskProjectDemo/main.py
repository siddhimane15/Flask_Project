from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about")
def aboutus():
    return render_template("aboutus.html")

@app.route("/contact")
def contactus():
    return render_template("contactus.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/socialmedia")
def socialmedia():
    return render_template("socialmedia.html")







app.run(debug=True)

