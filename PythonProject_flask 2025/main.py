from flask import Flask,render_template,request
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add")
def add():
    return render_template("add.html")    

@app.route("/result", methods=['POST'])
def result():
    a=int(request.form["txtFirst"])
    b=int(request.form["txtSecond"])
    c=a+b
    return render_template("result.html", answer=c)

@app.route("/Series")
def series():

    return render_template("series.html")    

@app.route("/marks")
def marks():
    return render_template("marks.html")

@app.route("/stud_result",methods=['POST'])
def stud_result():
    m=int(request.form['txtMarks'])
   
    return render_template("stud_result.html",result=status)






app.run()

