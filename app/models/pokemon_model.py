from app import mongo
from app.models.super_clase import SuperClass

class Pokemon(SuperClass): #La clase pokemon se esta heredando de la superclase
    def __init__(self): #Metodo super, hace referencia al padre SuperClase
      super().__init__("pokemons") #Los nombres de colecciones siempre deben ser iguales

      #ABSTRACCIÓN

    def create(self, data):
         raise NotImplementedError("Los pokemons bola no se pueden crear") #Lanza errores, forma en python raise
      
    def delete(self, object_id):
         raise NotImplementedError("Los pokemons bola no se pueden crear")
   
    def update(self, obect_id):
         raise NotImplementedError("Los pokemons bola no se pueden crear") #Lanza errores, forma en python r