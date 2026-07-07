
def calcular_media(numeros):            # Funcion para calcular la media
    total = sum(numeros)
    cantidad = len(numeros)
    
    media = total/cantidad
    return media


def calcular_mediana(numeros):          # Funcion para calcular la mediana
    ordenar = sorted(numeros)
    centro = len(numeros)//2
    mediana = ordenar[centro]
    
    return mediana

