from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def leer_criptograma(texto):
    path = "Criptograma/" + texto
    
    try:
         with open(path, 'rb') as archivo:
            return archivo.read()
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
            

def escribir_texto(nombre, texto_cifrado, carpeta_destino):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
 
    archivo_aes = os.path.join(carpeta_destino, nombre + ".txt")
    
    try:
        with open(archivo_aes, 'w') as texto_seguro:
            texto_seguro.write(texto_cifrado)  
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    
        
def aes_inverso(clave, texto_cifrado):
    iv = texto_cifrado[:16]
    cipher = Cipher(algorithms.AES(clave), modes.CFB(iv), backend=default_backend())
    descifrador = cipher.decryptor()
    texto_descifrado = descifrador.update(texto_cifrado[16:]) + descifrador.finalize() 
    return texto_descifrado.decode('utf-8')

def aplicamos_aes_inverso(nombre_original, texto_aes, clave):
    texto_aes = leer_criptograma(texto_aes)
    texto_desc = aes_inverso(clave, texto_aes)
    nombre = nombre_original
    escribir_texto(nombre, texto_desc, "Textoclaro")
 