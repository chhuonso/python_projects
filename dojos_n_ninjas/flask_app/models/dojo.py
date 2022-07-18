from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja


class Dojo: 
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL("dojos_and_ninjas").query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

        # ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name,created_at,updated_at) VALUES (%(name)s,NOW(),NOW());"
        result = connectToMySQL("dojos_and_ninjas").query_db(query,data)
        return result

    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls,data):
        query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id  = ninjas.dojos_id WHERE dojos.id = %(id)s' 

        result = connectToMySQL('dojos_and_ninjas').query_db(query,data)

        single_dojo = cls(result[0])
        if "ninjas.id" in result[0]:
            for ninja in result:
                ninja_data = {
                    "id": ninja["ninjas.id"],
                    "first_name": ninja["first_name"],
                    "last_name": ninja["last_name"],
                    "age": ninja["age"],
                    "created_at": ninja["created_at"],
                    "updated_at": ninja["updated_at"],
                    "dojos_id": ninja["dojos_id"]
                }
            single_dojo.ninjas.append(Ninja(ninja_data))
        return single_dojo
