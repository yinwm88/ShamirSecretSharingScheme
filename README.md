<div align="center">
  
# **Esquema de secreto compartido de Shamir** # 

</div>
<div>

  Es un algoritmo criptografico que hace posible que un solo dato pueda sser ocultado de manera que, a partir de él, se generan n diferentes datos y que con, al menos t ≤ n cualesquiera de ellos sea posible recuperar el dato original.
  > n es el total de integrantes con el que se compartira el texto, t es el minimo de estos integrantes para poder descifrar el texto.
  
</div>

<div>
  
# **Usage**   

</div>

- Crear un entorno virtual
- Instalar las paqueterias del requirements.txt:
  ```
    pip install -r requirements.txt
  ```
  - Clonar este repositorio:
  ```
   git clone https://github.com/yinwm88/ShamirSecretSharingScheme.git
  ```
- Entrar a la carpeta del repositorio clonado:
  ```
    git cd ShamirSecretSharingScheme
  ```
- Insertar en la carpeta Textoclaro el texto a cifrar.
- Para cifrar el texto y obttener las n evaluaciones, o para decirar un texto, corra:
  ```
   python Pgm/main.py
  ```
  - El programa corre en dos modalidades:
      - cifrar:
      ```
      c un_nombre_para_el_archivo_frg n t texto
      ```
      > el archivo frg es aquel que se generara y contendra las n evaluaciones, además de tener extesión .frg.
      
      - descifrar:
      ```
      d archivo_frg archivo_aes
      ```
      > el archivo_frg y el archivo_aes contendran el mismo nombre por default, el cual será el elegido previamente por el usuario. Pero este puede ser modificado sin problemas.    
