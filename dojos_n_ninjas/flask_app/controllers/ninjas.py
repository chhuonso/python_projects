from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/add_ninja') 
def add_new_ninja():
    print("NINJAS PATH")
    all_dojos = Dojo.get_all()
    return render_template('add_ninja.html', all_dojos = all_dojos) 

@app.route("/add_ninja/submit", methods=["POST"])
def new_ninja():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'age': request.form['age'],
        'dojos_id': request.form['dojos_id']
    }
    Ninja.create_new_ninja(data)
    return redirect("/")