def leer_eval(texto):
    listaEval = []
    texto_eval = "Eval/" + texto
    
    try:
        with open(texto_eval, 'r') as evaluaciones:
            for linea in evaluaciones:
                punto = linea.strip()
                componentes = punto.split(',')
                tupla = tuple(int(valor.strip('() ')) for valor in componentes)
                listaEval.append(tupla)
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
            
    return listaEval 