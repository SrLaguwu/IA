nombreArchivo = "C:/Users/eldia/OneDrive/Escritorio/IA/IA/Taller1/Prueba1.txt"

def leerArchivo(nombreArchivo):
    try:
        with open(nombreArchivo, "r") as archivo:
            for linea in archivo:
                print(linea, end="")
    except FileNotFoundError:
        print("No se pudo abrir el archivo.")

leerArchivo(nombreArchivo)



def mostrar_menuInicial():
    print("Selecciona una opción:")
    print("1. Busqueda NO informada")
    print("2. Busqueda informada")
    print("3. Salir")

def mostrar_menuNoInformada():
    print("Selecciona una opción:")
    print("1. Amplitud")
    print("2. Costo Uniforme")
    print("3. Profundidad evitando ciclos")
    print("4. Salir")

def mostrar_menuInformada():
    print("Selecciona una opción:")
    print("1. Avara")
    print("2. A*")
    print("3. Salir")

def seleccionar_opcion():
    opcion = input("Introduce la opción: ")
    return int(opcion)

while True:
    mostrar_menuInicial()
    opcion = seleccionar_opcion()

    if opcion == 1:
        print("Has seleccionado la opción de Busqueda No informada")

        while True:
            mostrar_menuNoInformada()
            opcion = seleccionar_opcion()
            if opcion == 1:
                print("Has seleccionado la opción de Busqueda NO informada por amplitud")

                #funcion de busqueda no informada por amplitud

            elif opcion == 2:
                print("Has seleccionado la opción de Busqueda No Informada de Costo Uniforme")

                #funcion de busqueda no informada por Costo Uniforme

            elif opcion == 3:
                print("Has seleccionado la opción de Busqueda No Informada de Profundidad evitando ciclos")

                #funcion de busqueda no informada por Profundidad evitando ciclos

            elif opcion == 4:
                print("¡Hasta luego!")
                break

            else:
                print("Opción no válida, por favor selecciona una opción válida.")



    elif opcion == 2:
        print("Has seleccionado la opción de Busqueda Informada")

        while True:
            mostrar_menuInformada()
            opcion = seleccionar_opcion()
            if opcion == 1:
                print("Has seleccionado la opción de Busqueda informada Avara")

                #funcion de busqueda informada por Avara

            elif opcion == 2:
                print("Has seleccionado la opción de Busqueda Informada A*")

                #funcion de busqueda informada por A*

            elif opcion == 3:
                print("¡Hasta luego!")
                break

            else:
                print("Opción no válida, por favor selecciona una opción válida.")



    elif opcion == 3:
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida, por favor selecciona una opción válida.")