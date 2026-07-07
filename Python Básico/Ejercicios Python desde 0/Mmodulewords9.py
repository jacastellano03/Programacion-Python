
def contar_palabras(texto, palabra):            # Contador de palabras
    list_palabras = texto.split()
    
    contador = 0
    
    for element in list_palabras:
        if element == palabra:
            contador += 1
        
    return contador             # El returncion debe ir siempre alineado con el for para que cuente los datos en este caso es un contador pero siempre debe ir alineado con el for para su correcto funcionamiento
    