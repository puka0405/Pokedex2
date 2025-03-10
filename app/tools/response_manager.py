from flask import jsonify 

class ResponseManager: 
    
    #SUCCES es la que nos dira que esta todo chido:)
    def success(self, data): #data, puede ser string
        if isinstance(data, str): #Si es una instancia de tipo
            data = { #Se sustituyte para que devuelva un objeto
                "message": data 
            }
        return jsonify(data), 200 #TODOO CHIDO
    
    #ERROR, es el que nos dira que esta todo mal por parte del usuario:(
    def error(self, data = "Invaid request"): 
        if isinstance(data, str): #Si es una instancia de tipo
            data = {
                "message": data
            }
        return jsonify(data), 400 #Error del usuario SONSOTE
    
    #ERROR_SERVER, es el que nos dira que esta todo mal por parte de nosotros:(
    def error_server(self, data = "SERVER ERROR"): 
        if isinstance(data, str): #Si es una instancia de tipo texto
            data = {
                "message": data
            }
        return jsonify(data), 500 #Error de nosotros, no del usuario 
    
    #axios - axios error - message tiene que venir del servidor