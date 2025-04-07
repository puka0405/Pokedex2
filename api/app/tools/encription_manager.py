import bcrypt

class EncryptionManager:
    def create_hash(self, text):
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(text.encode("utf-8"),salt).decode("utf-8") #UTF - tipo de decodificacion, tenemos manejo de acentos, coma, etc
    
    def compare_hash(self, text, hashpw):
        return bcrypt.checkpw(text.encode("utf-8"), hashpw.encode("utf-8")) #chewp nos devuelve un booleano, True o False