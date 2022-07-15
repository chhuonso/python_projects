# print("HELLOOOOO IM USERS ")
from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.user import User

@app.route("/")
def index():
    all_users = User.get_all()
    return render_template("index.html", all_users=all_users)


@app.route("/create")
def create_form():
    return render_template("create.html")


@app.route("/create/submit", methods=["POST"])
def submit_form():
    # print('submiited!!')
    # for key in request.form:
    #     print(f"{key}: {request.form[key]}")
    # User.save(request.form)
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email": request.form["email"],
    }
    User.save(data)
    return redirect("/")

@app.route("/users/<int:id>")
def single_user_page(id):
    data = {
        "id": id
    }
    result = User.find_one(data)
    print(result.first_name)
    return render_template("single.html", user=result)


@app.route("/users/<int:id>/delete")
def delete_user(id):
    print(f"trying to delete user#{id}")
    data = {
        "id":id
    }
    result = User.delete_one(data)
    return redirect("/")