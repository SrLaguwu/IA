from Nodo import Nodo
import time

matriz_de_nodos = []
nodo_a_expandir = 0

def verificar_posicion_nodo(nodo, x_, y_):
    if (nodo == None):
        return False
    else:
        if (nodo.x == x_ and nodo.y == y_):
            return True
        else:
            return False

def expandir(matriz_de_elementos, nodo, evitando_devolverse):
    IndexErrorXD = []

    if (nodo.grogu):
        return True
    else:
        try:
            if (evitando_devolverse == 2):
                if (verificar_posicion_nodo(nodo.padre, nodo.x + 1, nodo.y)):
                    IndexErrorXDXD = IndexErrorXD[0]

            if (nodo.x + 1 > 9):
                IndexErrorXDXD = IndexErrorXD[0]

            elemento = matriz_de_elementos[nodo.y][nodo.x + 1]
            grogu_ = nodo.grogu
            nave_ = nodo.nave
            operador_ = "Derecha"
            profundidad_ = nodo.profundidad + 1
            costo_ruta_ = nodo.costo_ruta

            if (elemento == 0):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (elemento == 1):
                IndexErrorXDXD = IndexErrorXD[0]
            elif (elemento == 2):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (elemento == 3):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1
                nave_ = 10

            elif (elemento == 4):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 5

            elif (elemento == 5):
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
            if (evitando_devolverse == 2):
                if (verificar_posicion_nodo(nodo.padre, nodo.x, nodo.y + 1)):
                    IndexErrorXDXD = IndexErrorXD[0]

            if (nodo.y + 1 > 9):
                IndexErrorXDXD = IndexErrorXD[0]
                                          
            elemento = matriz_de_elementos[nodo.y + 1][nodo.x]
            grogu_ = nodo.grogu
            nave_ = nodo.nave
            operador_ = "Abajo"
            profundidad_ = nodo.profundidad + 1
            costo_ruta_ = nodo.costo_ruta

            if (elemento == 0):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (elemento == 1):
                IndexErrorXDXD = IndexErrorXD[0]
            elif (elemento == 2):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (elemento == 3):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1
                nave_ = 10

            elif (elemento == 4):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 5

            elif (elemento == 5):
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
            if (evitando_devolverse == 2):
                if (verificar_posicion_nodo(nodo.padre, nodo.x, nodo.y - 1)):
                    IndexErrorXDXD = IndexErrorXD[0]

            if (nodo.y - 1 < 0):
                IndexErrorXDXD = IndexErrorXD[0]
                                          
            elemento = matriz_de_elementos[nodo.y - 1][nodo.x]
            grogu_ = nodo.grogu
            nave_ = nodo.nave
            operador_ = "Arriba"
            profundidad_ = nodo.profundidad + 1
            costo_ruta_ = nodo.costo_ruta

            if (elemento == 0):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (elemento == 1):
                IndexErrorXDXD = IndexErrorXD[0]
            elif (elemento == 2):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (elemento == 3):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1
                nave_ = 10

            elif (elemento == 4):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 5

            elif (elemento == 5):
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
            if (evitando_devolverse == 2):
                if (verificar_posicion_nodo(nodo.padre, nodo.x - 1, nodo.y)):
                    IndexErrorXDXD = IndexErrorXD[0]

            if (nodo.x - 1 < 0):
                IndexErrorXDXD = IndexErrorXD[0]
            # print("ss", nodo.y, nodo.x - 1, IndexErrorXDXD)

            elemento = matriz_de_elementos[nodo.y][nodo.x - 1]
            grogu_ = nodo.grogu
            nave_ = nodo.nave
            operador_ = "Izquierda"
            profundidad_ = nodo.profundidad + 1
            costo_ruta_ = nodo.costo_ruta

            if (elemento == 0):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (elemento == 1):
                IndexErrorXDXD = IndexErrorXD[0]
            elif (elemento == 2):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1

            elif (elemento == 3):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 1
                nave_ = 10

            elif (elemento == 4):
                if (nave_ > 0):
                    nave_ -= 1
                    costo_ruta_ += 0.5
                else:
                    costo_ruta_ += 5

            elif (elemento == 5):
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

        return False

def ejecutar(matriz_de_elementos, evitando_devolverse):    
    global matriz_de_nodos
    global nodo_a_expandir

    x_ = 0
    y_ = 0
    for y_inicial, fila in enumerate(matriz_de_elementos):
        for x_inicial, elemento in enumerate(fila):
            if elemento == 2:
                x_ = x_inicial
                y_ = y_inicial

    inicio = time.time()

    nodo_inicial = Nodo(x_, y_)

    matriz_de_nodos.append(nodo_inicial)

    grogu_encontrado = False

    while not(grogu_encontrado):
        print("x:",matriz_de_nodos[nodo_a_expandir].x, "- y:", matriz_de_nodos[nodo_a_expandir].y)
        print(matriz_de_elementos[matriz_de_nodos[nodo_a_expandir].y][matriz_de_nodos[nodo_a_expandir].x])
        print("nodo_a_expandir =", nodo_a_expandir)
        print("len(matriz_de_nodos) =", len(matriz_de_nodos))
        print("==================================================")
        # enter = input("==================================================")
        grogu_encontrado = expandir(matriz_de_elementos, matriz_de_nodos[nodo_a_expandir], evitando_devolverse)
        nodo_a_expandir += 1

    fin = time.time()
    tiempo_transcurrido = fin - inicio

    print("==================================================")

    nodos_expandidos = len(matriz_de_nodos)
    nodo_meta = nodo_a_expandir - 1

    nodoXD = matriz_de_nodos[nodo_meta]
    ruta_encontrada = nodoXD.operador
    while True:
        nodoXD = nodoXD.padre
        if (nodoXD.padre == None):
            break
        ruta_encontrada = nodoXD.operador + "->" + ruta_encontrada

    print("Nodos expandidos:", nodos_expandidos)
    print("Profundidad del arbol:", matriz_de_nodos[nodos_expandidos - 1].profundidad)
    print("Ruta:", ruta_encontrada)
    print("Costo de la ruta:", matriz_de_nodos[nodo_meta].costo_ruta)
    print("Tiempo de computo:", tiempo_transcurrido)

