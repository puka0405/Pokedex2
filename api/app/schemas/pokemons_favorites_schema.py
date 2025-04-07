from marshmallow import Schema, fields,ValidationError
#FIELDS, VALIDA TODOS 
class PokemonFavoriteSchema(Schema): 
    pokemon_id = fields.Str( #FIELDS, VALIDA TODOS 
        required = True, #lamda, funcion flecha de python
        validate = lambda x: len(x) > 0,
        error_messages={
            "required": "Upsi, el id del pokemo es requerido"
        }
    )

