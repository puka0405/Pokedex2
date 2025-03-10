#METODOS: CREATE, DELETE, GET id an all
from flask import Blueprint, request #Blueprint seccionar el servidor por carpetitas, Request maneja la peticion que haga el usuario, jsonify  response  
from marshmallow import ValidationError
from app.models.factory import ModelFactory #Traer la colección de usuarios
from bson import ObjectId #Formato que maneja mongo
from app.tools.response_manager import ResponseManager
from flask_jwt_extended import jwt_required #Decorador que se encarga de verificar si el token es valido

RM = ResponseManager()
bp = Blueprint("pokemon", __name__, url_prefix="/pokemons")  #Blueprint se instancea, secciona el servidor en carpetitas
pokemon_model = ModelFactory.get_model("pokemons") #Ir por el modelo de pokemones que ya declaramos

#OBTENER POR ID
@bp.route("/get/<string:pokemon_id>", methods = ["GET"])
@jwt_required()
def get_pokemon(pokemon_id):
    pokemon = pokemon_model.find_by_id(ObjectId(pokemon_id))
    return RM.success(pokemon)

#OBTENER TODOS

@bp.route("/get", methods = ["GET"])
@jwt_required()
def get_all():
   pokemon = pokemon_model.find_all()
   return RM.success(pokemon)

