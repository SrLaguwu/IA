from Nodo import Nodo
import time





matriz_de_elementos = [[]]
evitando_devolverse = 0
lista_de_nodos = []
nodo_a_expandir = 0
lista_hijos = []
pila_nodos = []





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


    nodo_ancestro = nodo_padre
    verificacion = True
    while verificacion:
        if (verificar_posicion_nodo(nodo_ancestro.padre, nodo_padre.x + x_, nodo_padre.y + y_)):
            IndexErrorXDXD = IndexErrorXD[0]
            
        else:
            nodo_ancestro= nodo_ancestro.padre
        if nodo_ancestro == None:
            verificacion = False



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
    global lista_hijos
    if (nodo.grogu):
        return True

    else:
        try:
            nuevo_nodo = crear_nodo(nodo, "Derecha")
            lista_de_nodos.append(nuevo_nodo)
            lista_hijos.append(nuevo_nodo)
        except IndexError:
            a = 0
            # print("¡Error! Índice fuera de rango.")

        try:
            nuevo_nodo = crear_nodo(nodo, "Abajo")
            lista_de_nodos.append(nuevo_nodo)
            lista_hijos.append(nuevo_nodo)
        except IndexError:
            a = 0
            # print("¡Error! Índice fuera de rango.")

        try:
            nuevo_nodo = crear_nodo(nodo, "Arriba")
            lista_de_nodos.append(nuevo_nodo)
            lista_hijos.append(nuevo_nodo)
        except IndexError:
            a = 0
            # print("¡Error! Índice fuera de rango.")

        try:
            nuevo_nodo = crear_nodo(nodo, "Izquierda")
            lista_de_nodos.append(nuevo_nodo)
            lista_hijos.append(nuevo_nodo)
        except IndexError:
            a = 0
            # print("¡Error! Índice fuera de rango.")
      
        return False





def ejecutar(matriz_de_elementos_):
    global matriz_de_elementos
    global lista_de_nodos
    global nodo_a_expandir

    matriz_de_elementos = matriz_de_elementos_
   
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

       # Inicializamos la pila con el nodo inicial
    pila_nodos = [nodo_inicial]

    nodo_actual = None

    nodos_expandidos = 0

    # Mientras no hayamos encontrado a Grogu y la pila no esté vacía
    while not grogu_encontrado and pila_nodos:
        # Tomamos el último nodo de la pila y lo expandimos
        nodo_actual = pila_nodos.pop(0)
        grogu_encontrado = expandir(nodo_actual)
        nodos_expandidos += 1
        # Insertamos los hijos al final de la pila para la búsqueda en profundidad
        pila_nodos = lista_hijos + pila_nodos
        # Limpiamos la lista de nodos hijos para la próxima iteración
        lista_hijos.clear()

        
    print("==================================================")


    fin = time.time()
    tiempo_transcurrido = fin - inicio


    print("==================================================")


    nodoXD = nodo_actual
    ruta_encontrada = nodoXD.operador
    while True:
        nodoXD = nodoXD.padre
        if (nodoXD.padre == None):
            break
        ruta_encontrada = nodoXD.operador + "->" + ruta_encontrada

    nodoMeta = nodo_actual
    ruta = []
    while nodoMeta:
        ruta.append(nodoMeta.operador)
        nodoMeta = nodoMeta.padre

    profundidad_del_arbol = 0
    for nodo_ in lista_de_nodos:
        if (nodo_.profundidad > profundidad_del_arbol):
            profundidad_del_arbol = nodo_.profundidad

    # Invierte la lista para obtener el orden correcto de los operadores
    ruta = ruta[::-1]
    # Elimina el primer elemento porque es None
    camino = ruta[1:]

    #Cantidad de nodos expandidos
    nodos_expandidos = nodos_expandidos


    nodos_creados = len(lista_de_nodos)
    lista_de_xy = [(nodo.x, nodo.y) for nodo in lista_de_nodos]
    #nodos expandidos, profundidad del árbol y tiempo de cómputo
    # print("ruta encontrada: ", camino)
    # print("lista de nodos creados: ", lista_de_xy)
    # print("Cantidad de nodos creados:", nodos_creados)
    print("Nodos expandidos:", nodos_expandidos)
    print("Profundidad del arbol:", profundidad_del_arbol)
    print("Tiempo de computo:", tiempo_transcurrido)


    return ruta_encontrada
