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


    def __lt__(self, otro_nodo):
        # Compara dos nodos basándose en su costo_ruta.
        # Devuelve True si el costo_ruta dereturn self.costo_ruta < otro.costo_ruta
        return self.costo_ruta < otro_nodo.costo_ruta

