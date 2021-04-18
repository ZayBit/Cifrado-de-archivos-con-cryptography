# Cifrado de archivos con cryptography
encripta archivos de forma de una forma sencilla,
si se agrega un archivo llamado **password.txt** que contenga una contraseña.

> **password.txt** tiene que ser creado antes de ejecutar **hidden.exe** por primera vez

> no hacer cambios al nombre de **hidden.exe**

La contraseña sera tomada encuenta una vez ya esten encriptados los archivos y vuelvas a iniciar **hidden.exe**

    dist>hidden.exe

### **Proceso:**
( :exclamation: ) para todas las carpetas que esten dentro de una de las carpetas principales , una carpeta dentro de otra no sera valida
- :file_folder: *folder 1*
    - file 1
    - etc
    - :file_folder: *sub folder* :exclamation:
        - **file 1**
        - **etc** 
- :file_folder: folder 2
    - file 1
    - etc
- **hidden.exe**
- file 1
- file 2
- etc.