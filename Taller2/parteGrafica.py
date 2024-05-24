import pygame
import sys
import random
import os


# Inicializar Pygame
pygame.init()

# Constantes para el tamaño
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = 75  # Tamaño de cada cuadrado del tablero 

# Crear la ventana de display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tablero de Ajedrez con Yoshis")

# Colores
WHITE = (255, 255, 255)
BLACK = (239, 239, 239)
HIGHLIGHT = (255, 255, 153)  # Color amarillo pastel para resaltar movimientos
GREEN = (144, 238, 144)  # Color verde pastel para Yoshi verde
RED = (255, 182, 193)    # Color rojo pastel para Yoshi rojo

# Cargar imágenes
yoshi_verde_original = pygame.image.load('images/yoshi_verde.png')
yoshi_rojo_original = pygame.image.load('images/yoshi_rojo.png')
yoshi_verde = pygame.transform.scale(yoshi_verde_original, (SQUARE_SIZE, SQUARE_SIZE))
yoshi_rojo = pygame.transform.scale(yoshi_rojo_original, (SQUARE_SIZE, SQUARE_SIZE))

# Cargar imágenes de victoria y derrota
def load_animation_frames(folder):
    frames = []
    for filename in sorted(os.listdir(folder)):
        if filename.endswith('.png'):
            img = pygame.image.load(os.path.join(folder, filename))
            frames.append(img)
    return frames

ganaste_frames = load_animation_frames('images/ganaste_frames')
perdiste_frames = load_animation_frames('images/perdiste_frames')

# Inicializar el diccionario de colores de casillas
square_colors = {}

def initialize_board_colors():
    """Inicializa el diccionario de colores de casillas con el patrón inicial de ajedrez."""
    for row in range(8):
        for col in range(8):
            square_colors[(row, col)] = WHITE if (row + col) % 2 == 0 else BLACK

def draw_board(yoshi_positions, possible_moves=None):
    """Dibuja un tablero de ajedrez 8x8 con los Yoshis y las casillas coloreadas."""
    for row in range(8):
        for col in range(8):
            color = square_colors[(row, col)]
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Resaltar movimientos posibles
    if possible_moves:
        for move in possible_moves:
            pygame.draw.rect(screen, HIGHLIGHT, (move[1] * SQUARE_SIZE, move[0] * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # Dibujar los Yoshis
    screen.blit(yoshi_verde, (yoshi_positions[0][1] * SQUARE_SIZE, yoshi_positions[0][0] * SQUARE_SIZE))
    screen.blit(yoshi_rojo, (yoshi_positions[1][1] * SQUARE_SIZE, yoshi_positions[1][0] * SQUARE_SIZE))

def get_random_positions():
    """Genera dos posiciones aleatorias y únicas para los Yoshis."""
    position1 = (random.randint(0, 7), random.randint(0, 7))
    position2 = (random.randint(0, 7), random.randint(0, 7))
    while position2 == position1:
        position2 = (random.randint(0, 7), random.randint(0, 7))
    return [position1, position2]

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

def draw_text(screen, text, position, font_size=36):
    """Dibuja el texto en la pantalla en la posición especificada."""
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, position)

def play_animation(screen, frames, duration):
    """Reproduce una secuencia de imágenes como una animación."""
    clock = pygame.time.Clock()
    start_time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - start_time < duration:
        for frame in frames:
            screen.fill(WHITE)  # Limpiar la pantalla
            screen.blit(frame, (WIDTH // 2 - frame.get_width() // 2, HEIGHT // 2 - frame.get_height() // 2))
            pygame.display.flip()
            clock.tick(10)  # Controla la velocidad de la animación (10 FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

def seleccionar_dificultad():
    
    while True:
        print("Seleccione la dificultad:")
        print("1. Principiante (arbol de profundidad 2)")
        print("2. Amateur (arbol de profundidad 4)")
        print("3. Experto (arbol de profundidad 6)")
        choice = input("Ingrese el número de la dificultad deseada: ")
        if choice in ["1", "2", "3"]:
            return int(choice)
        else:
            print("Selección inválida. Por favor, intente de nuevo.")

