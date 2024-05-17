import pygame
import sys
import random

# Inicializar Pygame
pygame.init()

# Constantes para el tamaño
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = 100  # Tamaño de cada cuadrado del tablero

# Crear la ventana de display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tablero de Ajedrez con Yoshis")

# Colores
WHITE = (255, 255, 255)
BLACK = (239, 239, 239)

# Cargar imágenes
yoshi_verde_original = pygame.image.load('images/yoshi_verde.png')
yoshi_rojo_original = pygame.image.load('images/yoshi_rojo.png')
yoshi_verde = pygame.transform.scale(yoshi_verde_original, (SQUARE_SIZE, SQUARE_SIZE))
yoshi_rojo = pygame.transform.scale(yoshi_rojo_original, (SQUARE_SIZE, SQUARE_SIZE))


def draw_board(yoshi_positions):
    """Dibuja un tablero de ajedrez 8x8 con dos Yoshis en posiciones aleatorias."""
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

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

def main():
    yoshi_positions = get_random_positions()

    # Bucle principal
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_board(yoshi_positions)
        pygame.display.flip()

if __name__ == "__main__":
    main()
