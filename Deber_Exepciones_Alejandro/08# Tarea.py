# Tarea 8
# Desarrolle un cajero automático que controle monto inválido, saldo insuficiente y entradas no numéricas.

saldo = 1000

try:
    monto = int(input('Ingrese el monto a retirar: '))
    
    if monto <= 0:
        raise Exception("El monto debe ser mayor que cero.")
    
    elif monto > saldo:
        raise Exception('Saldo Insuficiente.')
    
    print("Retiro realizado correctamente.")

except ValueError as e:
    print('Ingrese un valor numérico.')
    
except Exception as e:
    print(e)
    
