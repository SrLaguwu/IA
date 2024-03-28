from Nodo import Nodo
import heapq
import time

# Se inicializan listas vacías para almacenar la cola de prioridad y el nodo meta
cola_prioridad = []
nodo_meta = None

def verificar_posicion_nodo(nodo, x_, y_):
    # Esta función verifica si un nodo se encuentra en una posición (x_, y_) dada
    if nodo is None:
        return False
    elif nodo.x == x_ and nodo.y == y_:
        return True
    else:
        return False

def expandir(matriz_de_elementos, nodo, evitando_devolverse):
    global nodo_meta

    # Si el nodo actual es el nodo meta (con el elemento 'grogu'), se almacena en nodo_meta y se retorna True
    if nodo.grogu:
        nodo_meta = nodo
        return True
    else:
        # Expandir hacia la derecha
        try:
            # Si evitando_devolverse es 2 (evitar volver al nodo padre), se verifica si la posición a la derecha es el nodo padre
            if evitando_devolverse == 2 and verificar_posicion_nodo(nodo.padre, nodo.x + 1, nodo.y):
                pass
            # Si se sale de los límites de la matriz, se omite la expansión
            elif nodo.x + 1 > 9:
                pass
            else:
                # Se obtiene el elemento a la derecha del nodo actual
                elemento = matriz_de_elementos[nodo.y][nodo.x + 1]
                # Se calcula el costo de moverse a ese elemento
                costo_ruta_ = calcular_costo(elemento, nodo)
                # Si el costo no es None (es posible moverse ahí), se crea un nuevo nodo y se agrega a la cola de prioridad
                if costo_ruta_ is not None:
                    nuevo_nodo = Nodo(nodo.x + 1, nodo.y, elemento == 5, nodo.nave, nodo, "Derecha", nodo.profundidad + 1, costo_ruta_)
                    agregar_a_cola_prioridad(nuevo_nodo)
        except IndexError:
            pass

        # Expandir hacia abajo (el mismo proceso que para la derecha, pero con las coordenadas y + 1)
        try:
            if evitando_devolverse == 2 and verificar_posicion_nodo(nodo.padre, nodo.x, nodo.y + 1):
                pass
            elif nodo.y + 1 > 9:
                pass
            else:
                elemento = matriz_de_elementos[nodo.y + 1][nodo.x]
                costo_ruta_ = calcular_costo(elemento, nodo)
                if costo_ruta_ is not None:
                    nuevo_nodo = Nodo(nodo.x, nodo.y + 1, elemento == 5, nodo.nave, nodo, "Abajo", nodo.profundidad + 1, costo_ruta_)
                    agregar_a_cola_prioridad(nuevo_nodo)
        except IndexError:
            pass

        # Expandir hacia arriba (el mismo proceso, pero con las coordenadas y - 1)
        try:
            if evitando_devolverse == 2 and verificar_posicion_nodo(nodo.padre, nodo.x, nodo.y - 1):
                pass
            elif nodo.y - 1 < 0:
                pass
            else:
                elemento = matriz_de_elementos[nodo.y - 1][nodo.x]
                costo_ruta_ = calcular_costo(elemento, nodo)
                if costo_ruta_ is not None:
                    nuevo_nodo = Nodo(nodo.x, nodo.y - 1, elemento == 5, nodo.nave, nodo, "Arriba", nodo.profundidad + 1, costo_ruta_)
                    agregar_a_cola_prioridad(nuevo_nodo)
        except IndexError:
            pass

        # Expandir hacia la izquierda (el mismo proceso, pero con las coordenadas x - 1)
        try:
            if evitando_devolverse == 2 and verificar_posicion_nodo(nodo.padre, nodo.x - 1, nodo.y):
                pass
            elif nodo.x - 1 < 0:
                pass
            else:
                elemento = matriz_de_elementos[nodo.y][nodo.x - 1]
                costo_ruta_ = calcular_costo(elemento, nodo)
                if costo_ruta_ is not None:
                    nuevo_nodo = Nodo(nodo.x - 1, nodo.y, elemento == 5, nodo.nave, nodo, "Izquierda", nodo.profundidad + 1, costo_ruta_)
                    agregar_a_cola_prioridad(nuevo_nodo)
        except IndexError:
            pass

        # Si no se encontró el nodo meta, se retorna False
        return False

def calcular_costo(elemento, nodo):
    # Esta función calcula el costo de moverse a un elemento dado, considerando si se tiene una nave disponible
    nave_ = nodo.nave
    costo_ruta_ = nodo.costo_ruta

    if elemento == 0:
        if nave_ > 0:
            nave_ -= 1
            costo_ruta_ += 0.5
        else:
            costo_ruta_ += 1
    elif elemento == 1:
        return None  # No se puede expandir a un muro
    elif elemento == 2:
        if nave_ > 0:
            nave_ -= 1
            costo_ruta_ += 0.5
        else:
            costo_ruta_ += 1
    elif elemento == 3:
        if nave_ > 0:
            nave_ -= 1
            costo_ruta_ += 0.5
        else:
            costo_ruta_ += 1
        nave_ = 10  # Se recarga la nave
    elif elemento == 4:
        if nave_ > 0:
            nave_ -= 1
            costo_ruta_ += 0.5
        else:
            costo_ruta_ += 5  # Costo adicional por enemigo
    elif elemento == 5:
        if nave_ > 0:
            nave_ -= 1
            costo_ruta_ += 0.5
        else:
            costo_ruta_ += 1
        # Se alcanzó el nodo meta (grogu)

    return costo_ruta_

def agregar_a_cola_prioridad(nuevo_nodo):
    global cola_prioridad

    # Verificar si el nodo ya existe en la cola con un costo menor
    for nodo_existente in cola_prioridad:
        if nodo_existente[1].x == nuevo_nodo.x and nodo_existente[1].y == nuevo_nodo.y:
            if nodo_existente[1].costo_ruta <= nuevo_nodo.costo_ruta:
                return  # No agregar el nuevo nodo
            else:
                cola_prioridad.remove(nodo_existente)
                break

    # Agregar el nuevo nodo a la cola de prioridad, ordenado por costo
    heapq.heappush(cola_prioridad, (nuevo_nodo.costo_ruta, nuevo_nodo))

def ejecutar(matriz_de_elementos, evitando_devolverse=2):
    global cola_prioridad
    global nodo_meta

    # Encontrar la posición inicial (elemento 2)
    x_ = 0
    y_ = 0
    for y_inicial, fila in enumerate(matriz_de_elementos):
        for x_inicial, elemento in enumerate(fila):
            if elemento == 2:
                x_ = x_inicial
                y_ = y_inicial

    # Iniciar el conteo de tiempo
    inicio = time.time()

    # Crear el nodo inicial y agregarlo a la cola de prioridad
    nodo_inicial = Nodo(x_, y_)
    agregar_a_cola_prioridad(nodo_inicial)

    grogu_encontrado = False

    # Ciclo principal del algoritmo de búsqueda de costo uniforme
    while not grogu_encontrado:
        # Extraer el nodo con menor costo de la cola de prioridad
        nodo_a_expandir = heapq.heappop(cola_prioridad)[1]
        # Expandir el nodo y verificar si se encontró el nodo meta
        grogu_encontrado = expandir(matriz_de_elementos, nodo_a_expandir, evitando_devolverse)

    # Calcular el tiempo transcurrido
    fin = time.time()
    tiempo_transcurrido = fin - inicio

    print("==================================================")

    # Construir la ruta encontrada a partir del nodo meta
    ruta_encontrada = ""
    if nodo_meta.operador is not None:  # Verificar si el operador no es None
        ruta_encontrada = nodo_meta.operador
    nodoXD = nodo_meta.padre
    while True:
        if nodoXD is None:
            break
        if nodoXD.operador is not None:  # Verificar si el operador no es None
            ruta_encontrada = nodoXD.operador + "->" + ruta_encontrada
        nodoXD = nodoXD.padre

    # Imprimir los resultados
    print("Ruta:", ruta_encontrada)
    print("Costo de la ruta:", nodo_meta.costo_ruta)
    print(f"Tiempo de computo: {tiempo_transcurrido:.10f}")

    return ruta_encontrada