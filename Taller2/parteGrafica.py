import pygame
import sys
import os
from Nodo import Nodo
from Minimax import mejor_movimiento, minimax
from utils import initialize_board_colors, get_knight_moves, count_colored_squares, get_random_positions, square_colors, WHITE, GREEN, RED

# Inicializar Pygame
pygame.init()

# Constantes para el tamaño
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = 75  # Tamaño de cada cuadrado del tablero

# Crear la ventana de display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tablero de Ajedrez con Yoshis")

# Colores
BLACK = (239, 239, 239)
HIGHLIGHT = (255, 255, 153)  # Color amarillo pastel para resaltar movimientos

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
    yoshi_verde_pos = yoshi_positions[0]
    yoshi_rojo_pos = yoshi_positions[1]
    screen.blit(yoshi_verde, (yoshi_verde_pos[1] * SQUARE_SIZE, yoshi_verde_pos[0] * SQUARE_SIZE))
    screen.blit(yoshi_rojo, (yoshi_rojo_pos[1] * SQUARE_SIZE, yoshi_rojo_pos[0] * SQUARE_SIZE))

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

def main():
    dificultad = seleccionar_dificultad()
    max_depth = None  # Inicializamos max_depth como None para que pueda ser asignado más adelante
    if dificultad == 1:
        max_depth = 2
    elif dificultad == 2:
        max_depth = 4
    elif dificultad == 3:
        max_depth = 6
    else:
        print("Dificultad inválida. Saliendo del juego.")
        pygame.quit()
        sys.exit()

    yoshi_positions = get_random_positions()
    initialize_board_colors(yoshi_positions)
    selected_yoshi = None
    possible_moves = None
    turn = 0  # 0 para Yoshi verde, 1 para Yoshi rojo
    game_over = False
    winner_frames = None

    # initialize_board_colors()

    # Movimiento inicial de la IA
    if turn == 0:
        raiz = Nodo(yoshi_positions, turn, 0)
        ia_move = mejor_movimiento(raiz, max_depth)
        yoshi_positions[turn] = ia_move
        square_colors[ia_move] = GREEN
        turn = 1 - turn

    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouse_pos = pygame.mouse.get_pos()
                col = mouse_pos[0] // SQUARE_SIZE
                row = mouse_pos[1] // SQUARE_SIZE

                if (row, col) == yoshi_positions[turn]:
                    selected_yoshi = turn
                elif possible_moves and (row, col) in possible_moves:
                    yoshi_positions[selected_yoshi] = (row, col)
                    square_colors[(row, col)] = GREEN if selected_yoshi == 0 else RED
                    selected_yoshi = None
                    possible_moves = None
                    turn = 1 - turn  # Alternar turno

                    # Movimiento de la IA
                    if not game_over and turn == 0:
                        raiz = Nodo(yoshi_positions, turn, 0)
                        ia_move = mejor_movimiento(raiz, max_depth)
                        yoshi_positions[turn] = ia_move
                        square_colors[ia_move] = GREEN
                        turn = 1 - turn

                else:
                    selected_yoshi = None

                if selected_yoshi is not None:
                    possible_moves = get_knight_moves(yoshi_positions[selected_yoshi])
                else:
                    possible_moves = None

                # Verificar si no hay movimientos válidos para el próximo turno
                if not get_knight_moves(yoshi_positions[turn]):
                    game_over = True
                    winner_frames = ganaste_frames if turn == 1 else perdiste_frames

        draw_board(yoshi_positions, possible_moves)

        # Contar casillas pintadas y mostrar texto informativo
        green_count, red_count = count_colored_squares()
        info_text = f"Casillas Usuario: {red_count} , Casillas IA: {green_count}"
        draw_text(screen, info_text, (10, 10))

        pygame.display.flip()

        if game_over:
            play_animation(screen, winner_frames, 5000)  # Reproducir la animación durante 5 segundos
            pygame.time.wait(2000)  # Esperar 2 segundos antes de cerrar
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()