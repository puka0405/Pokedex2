from app import mongo
from app.models.super_clase import SuperClass

class Users(SuperClass):
    def __init__(self): 
        super().__init__("users")

    def find_all(self):
        raise NotImplementedError("No es necesario obtener todos los usuarios")
    
    def get_by_email(self, email):
        user = self.collection.find_one({"email": email})
        if user:
            user["_id"] = str(user["_id"])
        return user
    
    #A partir de una sola clase podamos traer cada clase de manera individul

    

