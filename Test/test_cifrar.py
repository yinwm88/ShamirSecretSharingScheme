import unittest
import os
import random
from cifrar import cifrar
from algoritmo_horner import algoritmo_horner
from obtener_coeficientes_aleatorios import obtener_coeficientes_aleatorios

def contar_lineas(nombre_eval):
    with open(nombre_eval, 'r') as archivo:
        lineas = [linea.strip() for linea in archivo if linea.strip()]
    return len(lineas)

class TestCifrar(unittest.TestCase):
    ''' 
        La funcion cifrar tiene la funcion principal de generar dos archivo, en 
        uno se contendran las n evaluaciones y en el otro el archivo cifrado con AES
        cada archivo debe terminar ya sea en .aes o en .frg.
        
        Ademas el archivo .frg debera contener n renglones, ya que n es el numero total de 
        integrantes de la junta.
        
        Ambos archivos deberan tener el mismo nombre y debera coincidir con el nombre elegido
        por el uuario para llamar al archivo con la n evaluaciones.
           
    '''
    cifrar("secreto", 5, 3, 'Textoclaro/texto_claro.txt')
    # esto generara dos archivos, uno con .frg y el otro .aes cada uno en sus respectivas carpetas

    def test_names(self):
        '''
            Prueba unitaria que verifica que los nombres de los archivos sea el mismo
            y solo cambien en la extension ademas de que coincida con el nombre elegido por el
            usuario para llamar al archivo con la evaluaciones.
        '''
        ruta_carpeta_cripto = "Criptograma"
        ruta_carpeta_eval = "Eval"
        nombre_elegido = "secreto"
        nombre_aes = nombre_elegido + ".aes"
        nombre_eval = nombre_elegido + ".frg"
            
        ruta_completa1 = os.path.join(ruta_carpeta_cripto, nombre_aes)
        ruta_completa2 = os.path.join(ruta_carpeta_eval, nombre_eval)
    
        self.assertTrue(os.path.exists(ruta_completa1) & os.path.exists(ruta_completa2), f"Los archivos {nombre_aes} y {nombre_eval} deberían existir en {ruta_carpeta}.")
    
    def test_rows(self):
        '''
            Prueba unitaria que verifica que el archivo .frg tenga todas las evaluaciones totales en cada renglon
            del archivo, las cualess correponderan a cada integrante de la junta(n)
        '''    
        ruta_eval = 'Eval/secreto.frg'
        resultado = contar_lineas(ruta_eval)
        self.assertEqual(resultado, 5, f"El número de evaluaciones totales debería ser 5." )

    '''
        Además también probaremos el algoritmo de Horner para asegurarnos de que efectivamente 
        evalua de manera inequivoca un polinomio, ademass de asegurarnos que el archivo .frg es
        correcto para poder usarlo al decifrar el informe.
    '''

    def test_horner(self):
        '''
            Prueba unitaria que verifica que el algoritmo de Horner se haya implementado de manera 
            correcta. Ademas de que k ea el termino independeiente del polinomio.
        ''' 
        n = 4
        t = 3
        k = 3
        coeficientes = []
        
        count = 0
        while t > 1:
            t = t - 1
            count = count+2 
            coeficientes.append(count)
        coeficientes.append(k) 
        # 2x^{2} + 4x + 3 
                 
        x = 0
        listaEval=[]
        while n > 0:
                x = x+1 #x=1, x=2, x=3, x=4
                y = algoritmo_horner(x, coeficientes)
                listaEval.append((x, y))
                n = n-1  

        self.assertEqual(listaEval, [(1, 9),(2, 19),(3, 33),(4, 51)], f"Algo anda mas con el algoritmo de Horner.") 
    
    def test_k_independiente(self):
        '''
            Prueba unitaria que verifica que k sea el termino independiente del polinomio.
        '''
        t = 3
        k = 3
        coeficientes = obtener_coeficientes_aleatorios(t, k)
        self.assertEqual(k, coeficientes[-1], f"k no es el termino independeiente del polinomio.")
    
    if __name__ == '__main__':
        unittest.main()