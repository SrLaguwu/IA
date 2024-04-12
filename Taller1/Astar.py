import heapq
from Nodo import Nodo
import time





def verificar_posicion_nodo(nodo, x_, y_):
    if (nodo == None):
        return False
    else:
        if (nodo.x == x_ and nodo.y == y_):
            return True
        else:
            return False





def h(nodo, x_meta, y_meta):
    return abs(nodo.x - x_meta) + abs(nodo.y - y_meta)





def expandir(nodo, x_meta, y_meta, matriz_de_elementos, evitando_devolverse, lista_de_nodos, heap_de_prioridad):
    if nodo.grogu:
        print("meta", nodo)
        return True
    
    else:
        for operador_ in ["Derecha", "Abajo", "Arriba", "Izquierda"]:
            try:
                nuevo_nodo = crear_nodo(nodo, operador_, x_meta, y_meta, matriz_de_elementos, evitando_devolverse)
                print("nn", nodo)
                lista_de_nodos.append(nuevo_nodo)
                # calculo del costo f, f(n) = g(n) + h(n)
                heapq.heappush(heap_de_prioridad, (nuevo_nodo.costo_ruta + h(nuevo_nodo, x_meta, y_meta), nuevo_nodo))
            except IndexError:
                pass

        return False





def crear_nodo(nodo_padre, operador_, x_meta, y_meta, matriz_de_elementos, evitando_devolverse):
    x_ = 0
    y_ = 0
    if (operador_ == "Derecha"):
        x_ += 1
        if (nodo_padre.x + x_ > 9):
            raise IndexError("Obstáculo encontrado")
    elif (operador_ == "Abajo"):
        y_ += 1
        if (nodo_padre.y + y_ > 9):
            raise IndexError("Obstáculo encontrado")
    elif (operador_ == "Arriba"):
        y_ -= 1
        if (nodo_padre.y + y_ < 0):
            raise IndexError("Obstáculo encontrado")
    elif (operador_ == "Izquierda"):
        x_ -= 1
        if (nodo_padre.x + x_ < 0):
            raise IndexError("Obstáculo encontrado")

    if (evitando_devolverse == 2):
        if (verificar_posicion_nodo(nodo_padre.padre, nodo_padre.x + x_, nodo_padre.y + y_)):
            raise IndexError("Evitando devolverse")

    elemento = matriz_de_elementos[nodo_padre.y + y_][nodo_padre.x + x_]
    grogu_ = nodo_padre.grogu
    nave_ = nodo_padre.nave
    profundidad_ = nodo_padre.profundidad + 1
    costo_ruta_ = nodo_padre.costo_ruta

    if (elemento == 0):
        if (nave_ > 0):
            nave_ -= 1
            costo_ruta_ += 0.5
        else:
            costo_ruta_ += 1
    elif (elemento == 1):
        raise IndexError("Obstáculo encontrado")
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





def ejecutar(matriz_de_elementos_, evitando_devolverse_):
    matriz_de_elementos = matriz_de_elementos_
    evitando_devolverse = evitando_devolverse_
    lista_de_nodos = []
    heap_de_prioridad = []

    x_ = 0
    y_ = 0
    x_meta = 0
    y_meta = 0
    for _y_, fila in enumerate(matriz_de_elementos):
        for _x_, elemento in enumerate(fila):
            if elemento == 2:
                x_ = _x_
                y_ = _y_
            if elemento == 5:
                x_meta = _x_
                y_meta = _y_

    inicio = time.time()

    nodo_inicial = Nodo(x_, y_)
    lista_de_nodos.append(nodo_inicial)
    heapq.heappush(heap_de_prioridad, (h(nodo_inicial, x_meta, y_meta), nodo_inicial))
    grogu_encontrado = False

    nodo_a_expandir_ref = None

    while not grogu_encontrado:
        nodo_a_expandir_ref = heapq.heappop(heap_de_prioridad)[1]
        grogu_encontrado = expandir(nodo_a_expandir_ref, x_meta, y_meta, matriz_de_elementos, evitando_devolverse, lista_de_nodos, heap_de_prioridad)

    fin = time.time()
    tiempo_transcurrido = fin - inicio

    print("==================================================")

    nodos_creados = len(lista_de_nodos)
    nodo_meta = len(lista_de_nodos) - 1

    # # # # # # nodo_actual = lista_de_nodos[nodo_meta]
    nodo_actual = nodo_a_expandir_ref
    ruta_encontrada = nodo_actual.operador
    while nodo_actual.padre is not None:
        ruta_encontrada = nodo_actual.operador + "->" + ruta_encontrada
        nodo_actual = nodo_actual.padre

    print("Nodos creados:", nodos_creados)
    print("Nodos expandidos:", nodo_meta + 1)
    print("Profundidad del árbol:", lista_de_nodos[nodo_meta].profundidad)
    print("Ruta:", ruta_encontrada)
    print("Costo de la ruta:", lista_de_nodos[nodo_meta].costo_ruta)
    print("Tiempo de cómputo:", tiempo_transcurrido)

    return ruta_encontrada
