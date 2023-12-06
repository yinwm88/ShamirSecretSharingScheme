import os
from Esquema.cifrar.cifrar import Cifrar
from Esquema.descifrar.descifrar import Descifrar


nombre_original = ''

def set_nombre_original(nombre):
      global nombre_original
      nombre_original = nombre    
  
def get_nombre_original():
      return nombre_original

# revisa los argumentos para cifrar
def checar_argumento_cifrar(argumentos):
      length = len(argumentos)
      if length == 5: 
            t = argumentos[3]
            n = argumentos[2]
            if n >= t :
                  return True
            else:
                  print(f"total:{n}")
                  print(f"minimo:{t}")
                  print("El minimo de personas para decifrar el texto excede al maximo de integrantes de la junta.")
                  print( f"{n}>={t}" )
                  return False
      else:
            print("No se cuenta con lo argumentos necesarios para cifrar.")
            return False
                              
                 
   #checar existecncia de esos archivos en sus respectivas carpetas, el eval y el criptograma            

def checar_argumento_descifrar(argumentos):
      length = len(argumentos)
      if length == 3: 
            return True
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
                  
                  nombre = os.path.splitext(nombre_texto_claro)[0]
                  set_nombre_original(nombre)
                  texto_claro = archivo_con_extension(nombre_texto_claro, ".txt")
                  
                  cifrador = Cifrar()    
                  cifrador.cifrar(nombre_guardar_eval, texto_claro, n, t)
                  print("CIFRADO EXITOSO.\n")
            else:
                  menu()
                  modalidad=input()
                  llamar_modalidad(modalidad)
                  
      elif comando == 'd':
            if checar_argumento_descifrar(argumentos):
                  nombre_eval= argumentos[1]
                  nombre_aes = argumentos[2]
                 
                  evaluaciones = archivo_con_extension(nombre_eval, ".frg")
                  criptograma = archivo_con_extension(nombre_aes, ".aes")
                  nombre_original = get_nombre_original() 
                  descifrador = Descifrar()
                  descifrador.descifrar(evaluaciones, criptograma, nombre_original)
                  print("DESCIFRADO EXITOSO.\n")
            else:
                  menu()
                  modalidad = input()
                  llamar_modalidad(modalidad)

      else:
            print("No existe esa modalidad.")
            menu()
            modalidad = input()
            llamar_modalidad(modalidad)