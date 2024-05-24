# utils.py

import pygame
import random

# Colores
WHITE = (255, 255, 255)
BLACK = (239, 239, 239)
HIGHLIGHT = (255, 255, 153)  # Color amarillo pastel para resaltar movimientos
GREEN = (144, 238, 144)  # Color verde pastel para Yoshi verde
RED = (255, 182, 193)    # Color rojo pastel para Yoshi rojo

# Inicializar el diccionario de colores de casillas
square_colors = {}

def initialize_board_colors():
    """Inicializa el diccionario de colores de casillas con el patrón inicial de ajedrez."""
    for row in range(8):
        for col in range(8):
            square_colors[(row, col)] = WHITE if (row + col) % 2 == 0 else BLACK

def get_knight_moves(position):
    """Calcula los movimientos válidos en forma de 'L' desde una posición dada, excluyendo casillas bloqueadas."""
    row, col = position
    moves = [
        (row + 2, col + 1), (row + 2, col - 1),
        (row - 2, col + 1), (row - 2, col - 1),
        (row + 1, col + 2), (row + 1, col - 2),
        (row - 1, col + 2), (row - 1, col - 2)
    ]
    valid_moves = [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8 and square_colors[(r, c)] in [WHITE, BLACK]]
    return valid_moves

def count_colored_squares():
    """Cuenta las casillas pintadas de verde y rojo."""
    green_count = sum(1 for color in square_colors.values() if color == GREEN)
    red_count = sum(1 for color in square_colors.values() if color == RED)
    return green_count, red_count

def get_random_positions():
    """Genera dos posiciones aleatorias y únicas para los Yoshis."""
    position1 = (random.randint(0, 7), random.randint(0, 7))
    position2 = (random.randint(0, 7), random.randint(0, 7))
    while position2 == position1:
        position2 = (random.randint(0, 7), random.randint(0, 7))
    return [position1, position2]
