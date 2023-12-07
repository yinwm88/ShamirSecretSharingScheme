import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
#from ..derivar_clave import derivar_clave


def leer_texto(texto):
    path = "../Textoclaro/" + texto
    with open(path, 'r') as archivo:
        return archivo.read()

def escribir_aes(nombre, texto_cifrado, carpeta_destino):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
 
    archivo_aes = os.path.join(carpeta_destino, nombre + ".aes")
    with open(archivo_aes, 'wb') as texto_seguro:
        texto_seguro.write(texto_cifrado)
    
def aes(texto_claro, clave):
    iv = os.urandom(16)  
    cipher = Cipher(algorithms.AES(clave), modes.CFB(iv), backend=default_backend())
    #clave necesita estar en formato de bytes 
    cifrador = cipher.encryptor()
    texto_cifrado = cifrador.update(texto_claro.encode('utf-8')) + cifrador.finalize()
    return iv + texto_cifrado


def aplicamos_aes(name_to_save, texto, clave):#la calve que recbimos es la calve derivada o la calve que se le aplico SHA
    #clave_derivada = derivar_clave(clave) #tal vez mejor solo le palicamos SHA y la convertimos a bytes
    texto_claro = leer_texto(texto);
    texto_cifrado = aes(texto_claro, clave)
    nombre = name_to_save
    escribir_aes(nombre, texto_cifrado, '../Criptograma')

def remove_texto_original(texto):
    ruta_archivo = "../Textoclaro/" + texto
    os.remove(ruta_archivo)
    print(f"\nLibre de evidencia: el archivo {ruta_archivo} fue eliminado.\nPara recuperarlo ingrese la opción de descifrar.\n")
 