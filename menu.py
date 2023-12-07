import os
from Esquema.cifrar.cifrar import Cifrar
from Esquema.descifrar.descifrar import Descifrar
import json

def checar_argumento_cifrar(argumentos):
    if len(argumentos) == 5:
          n = int(argumentos[2])
          if n>2:
            t = int(argumentos[3])
            if t <= n:
                   return True
            else:
                    print("El mínimo de personas para descifrar el texto excede al número de integrantes de la junta.")
          else:
                print("Se requiere que la junta tenga minimo 3 integrantes.")
    else:
        print("No se cuentan con los argumentos necesarios para cifrar.") 
    
    return False
                   
            
def existen_archivos(eval_file, aes_file):
    directorio_script = os.path.dirname(os.path.abspath(__file__))
      
    ruta_completa_eval = os.path.join(directorio_script, "Eval", eval_file)
    ruta_completa_aes = os.path.join(directorio_script, "Criptograma", aes_file)

    existe_eval = os.path.isfile(ruta_completa_eval)
    existe_aes = os.path.isfile(ruta_completa_aes)
    return existe_eval and existe_aes 

def checar_argumento_descifrar(argumentos):
      if len(argumentos) == 3: 
            eval_file = archivo_con_extension(argumentos[1],'.frg')
            aes_file = archivo_con_extension(argumentos[2], '.aes')
            if existen_archivos(eval_file, aes_file):
                  return True
            else:
                  print("Verifique que ambos archivos existan en las carpetas designadas para cada uno. ")
      else:
            print("No se cuenta con lo argumentos necesarios para descifrar.")
      
      return False
             

def archivo_con_extension(archivo, ext):
      extension = os.path.splitext(archivo)[1]
      if extension:
            return archivo 
      return archivo + ext
        
def menu():
    print("\nIngrese algunas de las siguientes opciones seguido de los argumentos necesarios según la modalidad elegida:\n")
    print("'c' para cifrar.")
    print("'d' para descifrar.")
    print("'s' para salir.\n")
    
    
def llamar_modalidad(modalidad):
      argumentos = modalidad.split()
      comando = argumentos[0]
      
      if comando == 's':
            print("FIN DEL PROGRAMA.\n")
            return
      
      if comando == 'c':
            if checar_argumento_cifrar(argumentos):
                  nombre_guardar_eval = argumentos[1]
                  n = int(argumentos[2])
                  t = int(argumentos[3])
                  nombre_texto_claro = argumentos[4] 
                  
                  #en de vez de set_name
                  nombre = os.path.splitext(nombre_texto_claro)[0]
                  with open("configuracion.json", "w") as config_file:
                        json.dump({"nombre_original": nombre}, config_file)

                  texto_claro = archivo_con_extension(nombre_texto_claro, ".txt")
                  
                  cifrador = Cifrar()    
                  cifrador.cifrar(nombre_guardar_eval, texto_claro, n, t)
                  print("CIFRADO EXITOSO.\n")
            else:
                  #no argumentos validos spara cifrar
                  menu()
                  modalidad=input()
                  llamar_modalidad(modalidad)
                  
      elif comando == 'd':
            if checar_argumento_descifrar(argumentos):
                  nombre_eval= argumentos[1]
                  nombre_aes = argumentos[2]
                 
                  evaluaciones = archivo_con_extension(nombre_eval, ".frg")
                  criptograma = archivo_con_extension(nombre_aes, ".aes")
            
                  #get name
                  with open("configuracion.json", "r") as config_file:
                        configuracion = json.load(config_file)
                   
                  nombre_original = configuracion.get("nombre_original", "")
                  
                  print(f"nombre original: {nombre_original}")
                  descifrador = Descifrar()
                  descifrador.descifrar(evaluaciones, criptograma, nombre_original)
                  print("\nDESCIFRADO EXITOSO.\n")
            else:
                  menu()
                  modalidad = input()
                  llamar_modalidad(modalidad)

      else:
            print("No existe esa modalidad.")
            menu()
            modalidad = input()
            llamar_modalidad(modalidad)