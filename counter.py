from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "LaLaMoo"

@app.route("/")
def index():
    session["count"] += 1
    return render_template("index.html")

@app.route("/plus_two")
def plus_two():
    session["count"] += 1
    return redirect("/")

@app.route("/reset")
def reset():
    session["count"] = -1
    return redirect("/")

count = 0

app.run(debug = True)
