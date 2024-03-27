class Nodo:
    def __init__(self, x, y, grogu=False, nave=0, padre=None, operador=None, profundidad=0, costo_ruta=0):
        self.grogu = grogu
        self.nave = nave

        self.padre = padre

        self.operador = operador
        self.x = x
        self.y = y

        self.profundidad = profundidad

        self.costo_ruta = costo_ruta

# Ejemplo de uso:
# Creamos un nodo inicial
nodo_inicial = Nodo(2, 3)

# # Creamos un nodo hijo con el nodo inicial como padre
# nodo_hijo = Nodo(estado=5, padre=nodo_inicial, operador="Derecha", profundidad=1, costo_ruta=10)

# # Imprimimos información del nodo hijo
# print("Estado:", nodo_hijo.estado)
# print("Padre:", nodo_hijo.padre.estado if nodo_hijo.padre else None)
# print("Operador:", nodo_hijo.operador)
# print("Profundidad:", nodo_hijo.profundidad)
# print("Costo de Ruta:", nodo_hijo.costo_ruta)
