#SOLAMENTE SE CREA Y SE ELIMINA
#MODIFICAR EL MODELO Y EVITAR QUE LOS USUARIOS USEN METODOS INDEBIDOS
#METODOS: CREATE, DELETE
from flask import Blueprint, request, jsonify #Blueprint seccionar el servidor por carpetitas, Request maneja la peticion que haga el usuario, jsonify  response  
from app.schemas.pokemons_favorites_schema import PokemonFavoriteSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory #Traer la colección de usuarios
from bson import ObjectId #Formato que maneja mongo
from app.tools.response_manager import ResponseManager
from flask_jwt_extended import jwt_required, get_jwt_identity #Decorador que se encarga de verificar si el token es valido


RM = ResponseManager()
bp = Blueprint("pokemon_favorite", __name__, url_prefix="/pokemon_favorite")
pokemon_favorite_schema = PokemonFavoriteSchema() #Instanciar
pokemon_favorite_model = ModelFactory.get_model("pokemon_favorite") #Ir por el modelo de POKEMONES FAVORITOS que ya declaramos

#CREAR
@bp.route("/create", methods=["POST"]) #
@jwt_required()
def create():
    user_id = get_jwt_identity()
    try:
        data = pokemon_favorite_schema.load(request.json) #Valida la informacion que se esta mandando, si algo anda mal va lanzar un error, error de validación "try, except"
        data["user_id"] = user_id
        pokemon_favorite_id = pokemon_favorite_model.create(data)  #Retorna el id insertado tipo especifico ObjectId
        return RM.success({"_id":str(pokemon_favorite_id)}) #200 es un código de respuesta

    except ValidationError as err:
        print(err)
        return RM.error("Upss, Los parametros enviados son incorrectos")#Espera dos argumentos un mensaje y un código "err 400"
    
#ELIMINAR

@bp.route("/delete/<string:pokemon_favorite_id>", methods = ["DELETE"]) #Va venir con parametro con la ruta
@jwt_required()
def delete(pokemon_favorite_id):
    pokemon_favorite_model.delete(ObjectId(pokemon_favorite_id)) #Esta recibiendo dos parametros, objectid
    return RM.success("Yeiii, pokemon eliminado con éxito jiji")

    #OBTENER

@bp.route("/get", methods = ["GET"])
@jwt_required()
def get_pokemon_favorite():
   user_id = get_jwt_identity()
   pokemon_favorite = pokemon_favorite_model.find_all(ObjectId(user_id))
   return RM.success(pokemon_favorite)

#MODIFICAR EL MODELO Y EVITAR QUE LOS USUARIOS USEN METODOS INDEBIDOS