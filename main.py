from flask import Flask,render_template,request

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

@app.route("/reg")
def registrationpage():
    return render_template("registration.html")



@app.route ("/success",methods=['POST'])
def successpage():
    n= request.form['txtName']
    m=request.form['txtMobile']
    return "<h1>Welcome:"+ n + "Mobile: "+ m  

@app.route("/square")
def square():
    return render_template("square.html")

@app.route("/result" ,methods=['POST'])
def result():
    n=int(request.form['txtNumber'])
    z=n*n
    return "Square is:"+str(z)

app.run(debug=True) 

