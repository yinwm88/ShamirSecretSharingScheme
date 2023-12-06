import unittest
import random
from Esquema.descifrar import get_k
from Esquema.cifrar import algoritmo_horner, obtener_coeficientes_aleatorios


primo = 208351617316091241234326746312124448251235562226470491514186331217050270460481

# La siguiente lista fue obtenida al leer un .frg donde las evaluaciones se obtuvieron
# de un polinomio con k=1000 como termino independiente
listaEval = [(1, 1561), (2, 2162), (3, 2803), (4, 3484), (5, 4205)]


class Testdescifra(unittest.TestCase):
    '''
        La clase descifra tiene el objetivo de devolver un archivo con
        el texto original, apartir del archivo con extensión .aes y del 
        archivo .frg.
        
        Para ello, se usa el algoritmo de Lagrange para obtener k (la clave 
        con la que se cifro el texto) de  las evaluacioines que estan en el 
        archivo .frg; y con k y el metodo aes_inverso, descifrar el archivo 
        .aes, generando el archivo .txt con el contentenido original y el nombre 
        original.
         
    '''
    
    def test_petenece_al_campo_finito(self):
        '''
            Verificar que la k obtenida con lagrange pertenece al campo finito
        ''' 
        rango = 0 <= get_k(listaEval) < primo
        self.assertTrue(rango, f"No pertenece al campo finito modulado por el numero primo.")
   
   
    def test_lagrange(self):
        '''
            Verificar que la k obtenida con lagrange coincide con el termino independeinete del polinomio del cual se obtuvo listaEval.
        ''' 
        k = get_k(listaEval) #en el metodo get_k se aplica el algoritmo de lagrange
        self.assertEqual(k, 1000, f"La k como termino independiente y la obtenida con el algoritmo de lagrange no coinciden.")
    
    def test_lagrange_denominador_no_cero(self):
        '''
            Verifica que en el .frg no haya parejas ordenadas repetidas.Ya que esto causara conflicto
            al momento de usar el algoritmo de lagrange para obtener k de vuelta.
            
        '''
        n = 50
        t = 30
        k = 100
        
        entrada_x = set()
        coeficientes = obtener_coeficientes_aleatorios(t, k)
        
        lista_eval=[]
        numeros_unicos = random.sample(range(1, 5000+1), n)
       
        for x in numeros_unicos:
            y = algoritmo_horner(x, coeficientes)
            lista_eval.append((x, y)) 
        
        for tupla in lista_eval:
            primera_entrada = tupla[0]
            if x in primera_entrada:
                return False
            return True
    
    if __name__ == '__main__':
        unittest.main()