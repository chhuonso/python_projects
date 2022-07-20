from pickle import FALSE
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import flash, re


# DATABASE = 'checklist'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#CHECKS and Validate REGISTER INFO
    @staticmethod
    def validate_user(user): 
        is_valid = True # ! we assume this is true

        if len(user['first_name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Passwords do not match")
            is_valid = False
        return is_valid

# ADDS users to the database
    @classmethod
    def save(cls, data):
        query = "INSERT INTO Users (first_name, last_name, email, password,created_at, updated_at) VALUES (%(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW());"
        return connectToMySQL("login_regist").query_db(query,data)


    #find the user by email
    @classmethod
    def get_one_by_email(cls,data):
        query = "SELECT * FROM Users WHERE email = %(email)s;"
        results = connectToMySQL("login_regist").query_db(query,data)  # gets back a list [Array[0]]
        if len(results) < 1:
            return False
        return cls(results[0])   #similar to else 



    @classmethod
    def get_one_by_id(cls,data):
        query = "SELECT * FROM Users WHERE id = %(id)s;"
        results = connectToMySQL("login_regist").query_db(query,data)
        return cls(results[0])