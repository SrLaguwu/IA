import Amplitud, juegoGrafico

nombreArchivo = "Prueba1.txt"

def leerArchivo(nombreArchivo):
    matriz = []
    try:
        with open(nombreArchivo, "r") as archivo:
            for linea in archivo:
                print(linea, end="")

                # elementos = linea.strip().split()  # Suponiendo que los elementos están separados por espacios en blanco
                elementos = [int(elemento) for elemento in linea.strip().split()]
                matriz.append(elementos)

    except FileNotFoundError:
        print("No se pudo abrir el archivo.")

    return matriz

matriz_de_elementos = leerArchivo(nombreArchivo)

# print(matriz_de_elementos)

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

programa_en_ejecucion = True

while programa_en_ejecucion:
    mostrar_menuInicial()
    opcion = seleccionar_opcion()

    if opcion == 1:
        print("\nHas seleccionado la opción de Busqueda No informada")

        while True:
            mostrar_menuNoInformada()
            opcion = seleccionar_opcion()
            if opcion == 1:

                #funcion de busqueda no informada por amplitud
                print("\nHas seleccionado la opción de Busqueda NO informada por Amplitud")
                print("Selecciona una opción:")
                print("1. NO evitando devolverse")
                print("2. Evitando devolverse")
                evitando_devolverse = seleccionar_opcion()
                ruta_final = Amplitud.ejecutar(matriz_de_elementos, evitando_devolverse)
                programa_en_ejecucion = False

                # Imprimir la salida de manera grafica
                opcion1 = "Busqueda no informada por Amplitud"
                if evitando_devolverse == 1:
                    opcion2 = "No evitando devolverse"
                    juegoGrafico.parteGrafica(ruta_final,matriz_de_elementos,opcion1,opcion2)

                if evitando_devolverse == 2:
                    opcion2 = "Evitando devolverse"
                    juegoGrafico.parteGrafica(ruta_final,matriz_de_elementos,opcion1,opcion2)
                break

            elif opcion == 2:
                print("\nHas seleccionado la opción de Busqueda NO Informada de Costo Uniforme")

                #funcion de busqueda no informada por Costo Uniforme

            elif opcion == 3:
                print("\nHas seleccionado la opción de Busqueda NO Informada de Profundidad evitando ciclos")

                #funcion de busqueda no informada por Profundidad evitando ciclos

            elif opcion == 4:
                # print("\n¡Hasta luego!\n")
                break

            else:
                print("\nOpción no válida, por favor selecciona una opción válida.")



    elif opcion == 2:
        print("\nHas seleccionado la opción de Busqueda Informada")

        while True:
            mostrar_menuInformada()
            opcion = seleccionar_opcion()
            if opcion == 1:
                print("\nHas seleccionado la opción de Busqueda informada Avara")

                #funcion de busqueda informada por Avara

            elif opcion == 2:
                print("\nHas seleccionado la opción de Busqueda Informada A*")

                #funcion de busqueda informada por A*

            elif opcion == 3:
                # print("\n¡Hasta luego!\n")
                break

            else:
                print("\nOpción no válida, por favor selecciona una opción válida.")



    elif opcion == 3:
        print("\n¡Hasta luego!\n")
        break

    else:
        print("\nOpción no válida, por favor selecciona una opción válida.")