
from Nodo import Nodo
from Minimax import *
from parteGrafica import *

def main():

    dificuldad = seleccionar_dificultad()
    if dificuldad == 1:
        # Aqui un metodo algoritmo_minimax que ejecute el algoritmo y tenga de parametro lo de la profundidad del arbol
        max_depth = 2

    elif dificuldad == 2:
        # Aquí x2
        max_depth = 4
        
    elif dificuldad == 3:
        # Aquí x3
        max_depth = 6

    yoshi_positions = get_random_positions()
    selected_yoshi = None
    possible_moves = None
    turn = 0  # 0 para Yoshi verde, 1 para Yoshi rojo
    game_over = False
    winner_frames = None

    initialize_board_colors()

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
        info_text = f"Casillas Usuario: {green_count} , Casillas IA: {red_count}"
        draw_text(screen, info_text, (10, 10))

        pygame.display.flip()

        if not game_over and turn == 1:  # Turno de la IA
            best_move = mejor_movimiento(yoshi_positions, turn, max_depth)
            yoshi_positions[turn] = best_move
            square_colors[best_move] = RED
            turn = 0  # Cambiar turno al jugador


        if game_over:
            play_animation(screen, winner_frames, 5000)  # Reproducir la animación durante 5 segundos
            pygame.time.wait(2000)  # Esperar 2 segundos antes de cerrar
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()