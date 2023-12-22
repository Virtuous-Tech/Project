from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/VirtuousFinance")
def VirtuousFinance():
    return render_template("Virtuous Finance.html")

@app.route("/VirtuousEducation")
def VirtuousEducation():
    return render_template("Virtuous Education.html")

@app.route("/ComingSoon")
def ComingSoon():
    return render_template("Coming Soon.html")

@app.route("/Python")
def Python():
    return render_template("Python.html")

@app.route("/HTMLCSS")
def HTMLCSS():
    return render_template("HTMLCSS.html")

@app.route("/Applications")
def Applications():
    return render_template("Applications.html")

    
if __name__ == "__main__":
    app.run(debug=True)