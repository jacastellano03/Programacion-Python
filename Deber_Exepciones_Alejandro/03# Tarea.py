# Tarea 3
# Solicite una lista de cinco números. Si alguno no es válido, vuelva a pedir únicamente ese dato.

def lista_numeros():
    
    lista = []
    
    for i in range(5):
        
        while True:
            
            try:
                numero = int(input('Ingresa un numero: '))
                lista.append(numero)
                break
                
            
            except ValueError as e:
                print(e)
                
    print(lista)
                
lista_numeros()
                