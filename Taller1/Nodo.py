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
