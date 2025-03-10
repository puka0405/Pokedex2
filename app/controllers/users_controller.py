#Ruteo
from flask import Blueprint, request #Blueprint seccionar el servidor por carpetitas, Request maneja la peticion que haga el usuario, jsonify  response  
from app.schemas.users_schema import UserSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory #Traer la colección de usuarios
from bson import ObjectId #Formato que maneja mongo
from app.tools.response_manager import ResponseManager
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token #jwr_required es un decorador que se encarga de verificar si el token es valido, 
#el get_jwt_identity es una funcion para obtener  y el create_access_token es para crear un token
from app.tools.encription_manager import EncryptionManager

RM = ResponseManager()
bp = Blueprint("users", __name__, url_prefix="/users")  #Blueprint se instancea, secciona el servidor en carpetitas
user_schema = UserSchema() #Instanciar
users_model = ModelFactory.get_model("users") #Ir por el modelo de ususarios que ya declaramos
EM = EncryptionManager()

#LOGEAR AL USUARIO

@bp.route("/login", methods=["POST"]) #Los ruteos reciben dos parametros, la ruta y los metodos que va a recibir
def login():
    data = request.json
    email = data.get("email",None) #.get viene del json, traeme la clave que tenga email, si no trae nada va a ser none
    password = data.get("password", None)
    if not email or not password:
      return RM.error("Upss, es necesario enviar todas las credenciales")
   
    user= users_model.get_by_email(email) #Va a traer el usuario si existe
    if not user:
        return RM.error("Upss, NO se encontro un usuario")
    if not EM.compare_hash(password, user["password"]):
        return RM.error("Upss, Credenciales invalidas") #PENDIENTE
    return RM.success({"user":user, "token":create_access_token(user["_id"])}) #Serializar cambiar de tipo

@bp.route("/register", methods=["POST"]) #
def register():
    try:
      print("ddddddddddddddddddddddddd",request.json)
      data = user_schema.load(request.json) #Valida la informacion que se esta mandando, si algo anda mal va lanzar un error, error de validación "try, except"
      data["password"]= EM.create_hash(data["password"]) #Encriptar la contraseña
      user_id = users_model.create(data)  #Retorna el id insertado tipo especifico ObjectId
      return RM.success({user_id:str(user_id), "token":create_access_token(str(user_id))}) #200 es un código de respuesta

    except ValidationError as err:
       print(err)
       return RM.error("Upss, Los parametros enviados son incorrectos")#Espera dos argumentos un mensaje y un código "err 400"  
    
    #ACTUALIZAR
            #Ruteo dinamico en la ruta 
@bp.route("/update", methods = ["PUT"])
@jwt_required() #Va venir con parametro con la ruta
def update():
    user_id = get_jwt_identity() #
    try:
        data = user_schema.load(request.json)
        data["password"]= EM.create_hash(data["password"]) #Encriptar la contraseña
        user= users_model.update(ObjectId(user_id), data) #Esta recibiendo dos parametros, objectid y no recuerdo el otro jaja
        return RM.success(user)
    except ValidationError as err: #ValidationError, se ejecuta o se dispara del schema
       return RM.error("Upss, Los parametros enviados son incorrectos") #Espera dos argumentos un mensaje y un código "err 400"  
    
    #ELIMINAR

@bp.route("/delete", methods = ["DELETE"])
@jwt_required() #Va venir con parametro con la ruta
def delete():
    user_id = get_jwt_identity()
    users_model.delete(ObjectId(user_id)) #Esta recibiendo dos parametros, objectid
    return RM.success("Usuario eliminado con exito")

    #OBTENER

@bp.route("/get", methods = ["GET"])
@jwt_required()
def get_user():
   user_id = get_jwt_identity()
   user = users_model.find_by_id(ObjectId(user_id))
   if not user:
      return RM.error("Chin, Usuario no encontrado")
   return RM.success(user)


    
