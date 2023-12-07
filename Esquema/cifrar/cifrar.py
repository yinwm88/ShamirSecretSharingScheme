from .obtener_evaluaciones import obtener_eval
from .aplica_aes import aplicamos_aes,remove_texto_original
from .obtener_coeficientes_aleatorios import obtener_coeficientes_aleatorio
import hashlib
import getpass

# clave_segura will be a string containing the hexadecimal
# representation of the SHA-256 hash of the input clave.
def aplicar_sha(clave):
    hash_object = hashlib.sha256()
    hash_object.update(clave.encode('utf-8'))
    #hash_hex = hash_object.hexdigest()
    clave_segura = hash_object.digest()#esto nos devolvera la calve 
    # en formato bytes que contendra la repressentacion binaria del sha aplicado a la calve
    return clave_segura



class Cifrar:


    def cifrar(self, name_to_save, texto, n, t):
        k_input = getpass.getpass("Ingresa tu contraseña: ")
        k = aplicar_sha(k_input)# nos devuelve la clave con SHA-256 en formato bytes 
        #set_salt()
        aplicamos_aes(name_to_save, texto, k)
        remove_texto_original(texto)

        #k_int = int(k, 16)
        k_int = int.from_bytes(k, byteorder='big') #convertimos una secuencia de bytes a un integer
        
        coeficientes = obtener_coeficientes_aleatorio(t, k_int)
        obtener_eval(n, coeficientes, name_to_save)
    