# Nodo.py
from utils import get_knight_moves, count_colored_squares

class Nodo:
    def __init__(self, yoshi_positions, turno, profundidad, padre=None):
        self.yoshi_positions = yoshi_positions  # Posiciones actuales de los Yoshi
        self.turno = turno  # Turno actual (0 yoshi verde y 1 yoshi rojo)
        self.profundidad = profundidad  # Profundidad del árbol
        self.padre = padre  # Nodo padre
        self.hijos = []  # Lista de hijos
        self.utilidad = None  # Puntaje del nodo que se calcula con la función de evaluación

    def guardar_hijo(self, nodo_hijo):
        self.hijos.append(nodo_hijo)

    # Revisa si es el nodo terminal, es decir que no haya movimientos posibles para el turno actual
    def es_terminal(self):
        return not get_knight_moves(self.yoshi_positions[self.turno])

    # Calcula la utilidad del nodo
    def evaluar(self):
        green_count, red_count = count_colored_squares()
        if self.turno == 0:  # Yoshi verde
            return green_count - red_count  # Yoshi verde maximiza
        else:
            return red_count - green_count  # Yoshi rojo maximiza
