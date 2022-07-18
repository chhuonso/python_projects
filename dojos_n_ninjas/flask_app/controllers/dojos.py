# print("HELLOOOOO IM USERS ")
from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/")
def index():
    all_dojos = Dojo.get_all()
    return render_template("index.html", all_dojos=all_dojos)

@app.route("/create")
def create_dojo():
    print("create form")
    return render_template("index.html")

@app.route("/create/submit", methods=["POST"])
def submit_dojo():
    data ={
        "name": request.form["name"]
    }
    Dojo.save(data)
    return redirect("/")

@app.route("/dojos/<int:id>")
def single_dojo_page(id):

    data = {
        "id":id
    }
    dojo = Dojo.get_one(data)
    print(dojo.name)
    return render_template("single.html", dojo=dojo)