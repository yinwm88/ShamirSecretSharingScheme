from .get_k import get_k
from .leer_eval import leer_eval
from .aplica_aes_inverso import aplicamos_aes_inverso

class Descifrar:
    
    def descifrar(self, texto_frg, texto_aes, nombre_original):
        listaEval = leer_eval(texto_frg)
        k_lagrange = get_k(listaEval)
        k_bytes = k_lagrange.to_bytes((k_lagrange.bit_length() + 7) // 8, byteorder='big')
        aplicamos_aes_inverso(nombre_original, texto_aes, k_bytes)

        