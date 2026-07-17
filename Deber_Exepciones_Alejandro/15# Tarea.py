# Tarea 15
# Desarrolle un menú repetitivo y controle opciones fuera del rango permitido.


while True:
    print('==== MENU ====')
    print('"1. Opción 1"')
    print("2. Opción 2")
    print("3. Salir")
    
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 3:
            raise Exception('Opción fuera del rango permitido.')
        
        if opcion == 1:
            print("Seleccionó la opción 1")
            
        if opcion ==2:
            print("Seleccionó la opción 2")
            
        if opcion ==3:
            print("Saliendo del programa...")
            break
            
    except ValueError:
        print('Ingrese una opción válida.')
        
    except Exception as e:
        print(e)