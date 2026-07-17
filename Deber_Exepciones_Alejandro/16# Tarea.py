# Tarea 16
# Cree una excepción personalizada llamada `StockInsuficienteError` y úsela en una función de venta.

class StockInsuficienteError(Exception):
    pass

def venta(stock, cantidad):
    if stock < cantidad:
        raise StockInsuficienteError('Stock insuficiente.')
    
    sobrante = stock - cantidad
    print(f"Venta realizada correctamente.")
    print(f"Stock restante: {sobrante}")

try:
    venta(100, 120)
    
except StockInsuficienteError as e:
    print(e)
    