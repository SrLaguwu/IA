from Nodo import Nodo

matriz_de_nodos = []
nodo_a_expandir = 0

def expandir(matriz_de_elementos, nodo):
    IndexErrorXD = []

    if (nodo.grogu):
        return True
    else:
        try:
            if (nodo.x + 1 > 9):
                IndexErrorXDXD = IndexErrorXD[0]

            p = matriz_de_elementos[nodo.y][nodo.x + 1]
            grogu_ = nodo.grogu
            nave_ = nodo.nave
            operador_ = "Derecha"
            profundidad_ = nodo.profundidad + 1
            costo_ruta_ = nodo.costo_ruta

            if (p == 0):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (p == 1):
                IndexErrorXDXD = IndexErrorXD[0]
            elif (p == 2):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (p == 3):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1
                nave_ = 10

            elif (p == 4):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 5

            elif (p == 5):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1
                grogu_ = True

            nuevo_nodo = Nodo(nodo.x + 1, nodo.y, grogu_, nave_, nodo, operador_, profundidad_, costo_ruta_)
            matriz_de_nodos.append(nuevo_nodo)
        except IndexError:
            a = 0
            # print("¡Error! Índice fuera de rango.")

        try:
            if (nodo.y + 1 > 9):
                IndexErrorXDXD = IndexErrorXD[0]

            p = matriz_de_elementos[nodo.y + 1][nodo.x]
            grogu_ = nodo.grogu
            nave_ = nodo.nave
            operador_ = "Abajo"
            profundidad_ = nodo.profundidad + 1
            costo_ruta_ = nodo.costo_ruta

            if (p == 0):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (p == 1):
                IndexErrorXDXD = IndexErrorXD[0]
            elif (p == 2):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (p == 3):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1
                nave_ = 10

            elif (p == 4):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 5

            elif (p == 5):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1
                grogu_ = True

            nuevo_nodo = Nodo(nodo.x, nodo.y + 1, grogu_, nave_, nodo, operador_, profundidad_, costo_ruta_)
            matriz_de_nodos.append(nuevo_nodo)
        except IndexError:
            a = 0
            # print("¡Error! Índice fuera de rango.")

        try:
            if (nodo.y - 1 < 0):
                IndexErrorXDXD = IndexErrorXD[0]

            p = matriz_de_elementos[nodo.y - 1][nodo.x]
            grogu_ = nodo.grogu
            nave_ = nodo.nave
            operador_ = "Arriba"
            profundidad_ = nodo.profundidad + 1
            costo_ruta_ = nodo.costo_ruta

            if (p == 0):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (p == 1):
                IndexErrorXDXD = IndexErrorXD[0]
            elif (p == 2):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (p == 3):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1
                nave_ = 10

            elif (p == 4):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 5

            elif (p == 5):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1
                grogu_ = True

            nuevo_nodo = Nodo(nodo.x, nodo.y - 1, grogu_, nave_, nodo, operador_, profundidad_, costo_ruta_)
            matriz_de_nodos.append(nuevo_nodo)
        except IndexError:
            a = 0
            # print("¡Error! Índice fuera de rango.")

        try:
            if (nodo.x - 1 < 0):
                IndexErrorXDXD = IndexErrorXD[0]
            # print("ss", nodo.y, nodo.x - 1, IndexErrorXDXD)

            p = matriz_de_elementos[nodo.y][nodo.x - 1]
            grogu_ = nodo.grogu
            nave_ = nodo.nave
            operador_ = "Izquierda"
            profundidad_ = nodo.profundidad + 1
            costo_ruta_ = nodo.costo_ruta

            if (p == 0):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (p == 1):
                IndexErrorXDXD = IndexErrorXD[0]
            elif (p == 2):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (p == 3):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1
                nave_ = 10

            elif (p == 4):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 5

            elif (p == 5):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1
                grogu_ = True

            nuevo_nodo = Nodo(nodo.x - 1, nodo.y, grogu_, nave_, nodo, operador_, profundidad_, costo_ruta_)
            matriz_de_nodos.append(nuevo_nodo)
        except IndexError:
            a = 0
            # print("¡Error! Índice fuera de rango.")


        # # # # if (nodo.y > 0 and nodo.x > 0 and nodo.y < 9 and nodo.x < 9):
        # # # #     if(matriz_de_elementos[nodo.y][nodo.x + 1] != 1):
        # # # #         print("xd:",matriz_de_elementos[nodo.y][nodo.x + 1])
        # # # #     elif(matriz_de_elementos[nodo.y + 1][nodo.x] != 1):
        # # # #         print("xd:", matriz_de_elementos[nodo.y + 1][nodo.x])
        # # # #     elif(matriz_de_elementos[nodo.y - 1][nodo.x] != 1):
        # # # #         print("xd:", matriz_de_elementos[nodo.y - 1][nodo.x])
        # # # #     else:
        # # # #         print("xd:", matriz_de_elementos[nodo.y][nodo.x - 1])

        # # # # elif (nodo.y == 0 and nodo.x == 0):
        # # # #     if(matriz_de_elementos[nodo.y][nodo.x + 1] != 1):
        # # # #         print("xd:",matriz_de_elementos[nodo.y][nodo.x + 1])
        # # # #     else:
        # # # #         print("xd:", matriz_de_elementos[nodo.y + 1][nodo.x])

        # # # # elif (nodo.y == 9 and nodo.x == 9):
        # # # #     if(matriz_de_elementos[nodo.y - 1][nodo.x] != 1):
        # # # #         print("xd:",matriz_de_elementos[nodo.y - 1][nodo.x])
        # # # #     else:
        # # # #         print("xd:", matriz_de_elementos[nodo.y][nodo.x - 1])

        # # # # elif (nodo.y == 0 and nodo.x == 9):
        # # # #     if(matriz_de_elementos[nodo.y + 1][nodo.x] != 1):
        # # # #         print("xd:",matriz_de_elementos[nodo.y + 1][nodo.x])
        # # # #     else:
        # # # #         print("xd:", matriz_de_elementos[nodo.y][nodo.x - 1])

        # # # # elif (nodo.y == 9 and nodo.x == 0):
        # # # #     if(matriz_de_elementos[nodo.y][nodo.x + 1] != 1):
        # # # #         print("xd:",matriz_de_elementos[nodo.y][nodo.x + 1])
        # # # #     else:
        # # # #         print("xd:", matriz_de_elementos[nodo.y - 1][nodo.x])

        # # # # elif (nodo.y == 0):
        # # # #     if(matriz_de_elementos[nodo.y][nodo.x + 1] != 1):
        # # # #         print("xd:",matriz_de_elementos[nodo.y][nodo.x + 1])
        # # # #     elif(matriz_de_elementos[nodo.y + 1][nodo.x] != 1):
        # # # #         print("xd:", matriz_de_elementos[nodo.y + 1][nodo.x])
        # # # #     else:
        # # # #         print("xd:", matriz_de_elementos[nodo.y][nodo.x - 1])

        # # # # elif (nodo.x == 0):
        # # # #     if(matriz_de_elementos[nodo.y][nodo.x + 1] != 1):
        # # # #         print("xd:",matriz_de_elementos[nodo.y][nodo.x + 1])
        # # # #     elif(matriz_de_elementos[nodo.y + 1][nodo.x] != 1):
        # # # #         print("xd:", matriz_de_elementos[nodo.y + 1][nodo.x])
        # # # #     else:
        # # # #         print("xd:", matriz_de_elementos[nodo.y - 1][nodo.x])

        # # # # elif (nodo.y == 9):
        # # # #     if(matriz_de_elementos[nodo.y][nodo.x + 1] != 1):
        # # # #         print("xd:",matriz_de_elementos[nodo.y][nodo.x + 1])
        # # # #     elif(matriz_de_elementos[nodo.y - 1][nodo.x] != 1):
        # # # #         print("xd:", matriz_de_elementos[nodo.y - 1][nodo.x])
        # # # #     else:
        # # # #         print("xd:", matriz_de_elementos[nodo.y][nodo.x - 1])

        # # # # elif (nodo.x == 9):
        # # # #     if(matriz_de_elementos[nodo.y + 1][nodo.x] != 1):
        # # # #         print("xd:",matriz_de_elementos[nodo.y + 1][nodo.x])
        # # # #     elif(matriz_de_elementos[nodo.y - 1][nodo.x] != 1):
        # # # #         print("xd:", matriz_de_elementos[nodo.y - 1][nodo.x])
        # # # #     else:
        # # # #         print("xd:", matriz_de_elementos[nodo.y][nodo.x - 1])

        return False

def ejecucion(matriz_de_elementos):

    x_ = 0
    y_ = 0
    for y_inicial, fila in enumerate(matriz_de_elementos):
        for x_inicial, elemento in enumerate(fila):
            if elemento == 2:
                x_ = x_inicial
                y_ = y_inicial

    nodo_inicial = Nodo(x_, y_)

    global matriz_de_nodos
    matriz_de_nodos.append(nodo_inicial)
    global nodo_a_expandir

    grogu_encontrado = False

    nodo_meta = 0

    while not(grogu_encontrado):
        grogu_encontrado = expandir(matriz_de_elementos, matriz_de_nodos[nodo_a_expandir])
        print("x:",matriz_de_nodos[nodo_a_expandir].x, "- y:", matriz_de_nodos[nodo_a_expandir].y)
        print(matriz_de_elementos[matriz_de_nodos[nodo_a_expandir].y][matriz_de_nodos[nodo_a_expandir].x])
        nodo_a_expandir += 1
        print("len(matriz_de_nodos)", len(matriz_de_nodos))
        print("nodo_a_expandir", nodo_a_expandir)
        print("==================================================")
        # enter = input("==================================================")

    for xddd in matriz_de_nodos:
        print("x:",xddd.x, "- y:", xddd.y, "- p:", xddd.profundidad, "\n")

    print("///")

    nodo_meta = nodo_a_expandir - 1
    nodoXD = matriz_de_nodos[nodo_meta]

    while nodoXD.padre != None:
        print(nodoXD.operador)
        nodoXD = nodoXD.padre

    # print(nodo_inicial.grogu)
    # print(nodo_inicial.nave)
    # print(nodo_inicial.padre)
    # print(nodo_inicial.operador)
    # print(nodo_inicial.x)
    # print(nodo_inicial.y)
    # print(nodo_inicial.profundidad)
    # print(nodo_inicial.costo_ruta)
    # print(nodo_inicial)
    # print(matriz_de_nodos)
