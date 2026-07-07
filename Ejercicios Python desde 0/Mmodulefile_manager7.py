
# Cómo escribir un archivo

archivo = open ("texto.txt", "w")       # "texto.txt" → nombre del archivo, "w" → modo escritura

archivo.write('Hola Python!!')          # Aqui se escribe texto dentro del archivo.

archivo.close()                         # MUY importante. Cierra el archivo.

# Esto debe crear un archivo de tipo texto en nuestra carpeta.



# Cómo leer un archivo

archivo = open ("texto.txt", "r")       # Cuando vamos a leer debemos cambiar la w por r (read = leer)

contenido = archivo.read()              # Creamos una variable contenido que agarra todo el texto del archivo y lo guarda.

print(contenido)                        # Utilizo priint que lo muestra en pantalla.

archivo.close()                         # De igual manera debemos concluir cerrando el archivo






def escribir_archivo(nombre, texto):
    
    archivo = open (nombre, "w")
    
    archivo.write(texto)
    
    archivo.close()
    

def leer_archivo(nombre):
    
    archivo = open (nombre, "r")
    
    contenido = archivo.read()
    
    print(contenido)
    
    archivo.close()
    
    