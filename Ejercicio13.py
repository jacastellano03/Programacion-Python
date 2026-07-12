# Ejercicio de clase 13
# Cree una excepción personalizada llamada MontoInvalidoError y úsela en una función de pago.

class MontoInvalidoError(Exception):
    pass

def realizar_pago():

    try:
        monto = float(input("Ingrese el monto a pagar: "))

        if monto <= 0:
            raise MontoInvalidoError("El monto debe ser mayor que cero.")

        print("Pago realizado correctamente.")
        print("Monto pagado:", monto)

    except MontoInvalidoError as e:
        print(e)

    except ValueError:
        print("Debe ingresar un valor numérico.")

realizar_pago()