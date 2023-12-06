import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

salt = b'' # Inicializamos salt como bytes vacíos

def set_salt():
    global salt
    salt = os.urandom(16)

def get_salt(): 
    return salt

def derivar_clave(k):
    k_bytes = k.encode() #convierte k en bytes usando UTF-8
    contraseña_derivada = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        salt = get_salt(),
        iterations=100000,
        length=32,
    )
    clave_derivada = contraseña_derivada.derive(k_bytes)
    return clave_derivada
