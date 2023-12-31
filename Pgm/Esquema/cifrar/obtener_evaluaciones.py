import os
import random
from .algoritmo_horner import algoritmo_horner

def obtener_eval(n, coeficientes, name_file_save):
    listaEval=[]
    numeros_unicos = random.sample(range(1, 10000+1), n)
    for x in numeros_unicos:
        y = algoritmo_horner(x, coeficientes)
        listaEval.append((x, y)) 
        
    if not os.path.exists("Eval"):
        os.makedirs("Eval")
    name = name_file_save + ".frg"
    archivo_frg = os.path.join("Eval", name)
    
    try:
        with open(archivo_frg, 'w') as evaluaciones:
            for evaluacion in listaEval:
                 evaluaciones.write(f"{evaluacion}\n")  
                 
    except FileNotFoundError as e:
        print(f"Error: {e}")
            
    
     
