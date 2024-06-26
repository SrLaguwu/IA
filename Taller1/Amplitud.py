from Nodo import Nodo
import time




matriz_de_elementos = [[]]
evitando_devolverse = 0
lista_de_nodos = []
nodo_a_expandir = 0





def verificar_posicion_nodo(nodo, x_, y_):
    if (nodo == None):
        return False
    else:
        if (nodo.x == x_ and nodo.y == y_):
            return True
        else:
            return False





def crear_nodo(nodo_padre, operador_):
        global matriz_de_elementos
        global evitando_devolverse
        
        
        IndexErrorXD = []


        x_ = 0
        y_ = 0
        if (operador_ == "Derecha"):
            x_ += 1
            if (nodo_padre.x + x_ > 9):
                IndexErrorXDXD = IndexErrorXD[0]
        elif (operador_ == "Abajo"):
            y_ += 1
            if (nodo_padre.y + y_ > 9):
                IndexErrorXDXD = IndexErrorXD[0]
        elif (operador_ == "Arriba"):
            y_ -= 1
            if (nodo_padre.y + y_ < 0):
                IndexErrorXDXD = IndexErrorXD[0]
        elif (operador_ == "Izquierda"):
            x_ -= 1
            if (nodo_padre.x + x_ < 0):
                IndexErrorXDXD = IndexErrorXD[0]


        if (evitando_devolverse == 2):
            if (verificar_posicion_nodo(nodo_padre.padre, nodo_padre.x + x_, nodo_padre.y + y_)):
                IndexErrorXDXD = IndexErrorXD[0]


        elemento = matriz_de_elementos[nodo_padre.y + y_ ][nodo_padre.x + x_]
        grogu_ = nodo_padre.grogu
        nave_ = nodo_padre.nave
        # operador_ = "Derecha"
        # operador_ = "Abajo"
        # operador_ = "Arriba"
        # operador_ = "Izquierda"
        profundidad_ = nodo_padre.profundidad + 1
        costo_ruta_ = nodo_padre.costo_ruta


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


        return Nodo(nodo_padre.x + x_, nodo_padre.y + y_, grogu_, nave_, nodo_padre, operador_, profundidad_, costo_ruta_)





def expandir(nodo):
    if (nodo.grogu):
        return True

    else:
        try:
            nuevo_nodo = crear_nodo(nodo, "Derecha")
            lista_de_nodos.append(nuevo_nodo)
        except IndexError:
            a = 0
            # print("¡Error! Índice fuera de rango.")

        try:
            nuevo_nodo = crear_nodo(nodo, "Abajo")
            lista_de_nodos.append(nuevo_nodo)
        except IndexError:
            a = 0
            # print("¡Error! Índice fuera de rango.")

        try:
            nuevo_nodo = crear_nodo(nodo, "Arriba")
            lista_de_nodos.append(nuevo_nodo)
        except IndexError:
            a = 0
            # print("¡Error! Índice fuera de rango.")

        try:
            nuevo_nodo = crear_nodo(nodo, "Izquierda")
            lista_de_nodos.append(nuevo_nodo)
        except IndexError:
            a = 0
            # print("¡Error! Índice fuera de rango.")


        return False





def ejecutar(matriz_de_elementos_, evitando_devolverse_):
    global matriz_de_elementos
    global evitando_devolverse
    global lista_de_nodos
    global nodo_a_expandir


    matriz_de_elementos = matriz_de_elementos_
    evitando_devolverse = evitando_devolverse_


    x_ = 0
    y_ = 0
    for _y_, fila in enumerate(matriz_de_elementos):
        for _x_, elemento in enumerate(fila):
            if elemento == 2:
                x_ = _x_
                y_ = _y_


    inicio = time.time()


    nodo_inicial = Nodo(x_, y_)
    lista_de_nodos.append(nodo_inicial)
    grogu_encontrado = False


    print("\n==================================================")


    while not(grogu_encontrado):
        # print("Informacion del nodo a expandir")
        # print("Nodo a expandir #" + str(nodo_a_expandir))
        # print("x:",lista_de_nodos[nodo_a_expandir].x, "| y:", lista_de_nodos[nodo_a_expandir].y)
        # print("Elemento encontrado:", matriz_de_elementos[lista_de_nodos[nodo_a_expandir].y][lista_de_nodos[nodo_a_expandir].x])
        grogu_encontrado = expandir(lista_de_nodos[nodo_a_expandir])
        # print("Total de nodos creados despues de la expansion del nodo a expandir #" + str(nodo_a_expandir)+ ":", len(lista_de_nodos))
        # print("==================================================")
        # # enter = input("==================================================")
        nodo_a_expandir += 1


    fin = time.time()
    tiempo_transcurrido = fin - inicio


    print("==================================================")


    nodos_creados = len(lista_de_nodos)
    nodo_meta = nodo_a_expandir - 1

    nodoXD = lista_de_nodos[nodo_meta]
    ruta_encontrada = nodoXD.operador
    while True:
        nodoXD = nodoXD.padre
        if (nodoXD.padre == None):
            break
        ruta_encontrada = nodoXD.operador + "->" + ruta_encontrada

    # print("Nodos creados:", nodos_creados)
    print("Nodos expandidos:", nodo_meta + 1)
    print("Profundidad del arbol:", lista_de_nodos[nodos_creados - 1].profundidad)
    # print("Ruta:", ruta_encontrada)
    # print("Costo de la ruta:", lista_de_nodos[nodo_meta].costo_ruta)
    print("Tiempo de computo:", tiempo_transcurrido)


    return ruta_encontrada
