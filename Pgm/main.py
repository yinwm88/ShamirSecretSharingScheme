from menu import llamar_modalidad


if __name__ == "__main__":

    modalidad = input(" \nIngrese algunas de las siguientes opciones seguido de los argumentos necesarios según la modalidad elegida:\n \n'c' para cifrar. \n'd' para descifrar. \n's' para salir.\n")  
    llamar_modalidad(modalidad)
