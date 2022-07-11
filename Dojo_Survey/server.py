from crypt import methods
from tkinter import Widget
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "button"


@app.route("/")
def index():
    return render_template("/index.html")

@app.route("/results")
def result():
    return render_template("/results.html")

@app.route("/result", methods=['post'])
def submit():
    session['full_name'] = request.form['full_name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    print(request.form)
    return redirect("/results")

if __name__=="__main__":
    app.run(debug=True)