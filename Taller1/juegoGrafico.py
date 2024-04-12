import pygame

pygame.init()

def parteGrafica(ruta_final,matriz_de_elementos, opcion1, opcion2 = None):

    ancho = 800
    alto = 800
    pantalla = pygame.display.set_mode((ancho, alto))
    if(opcion2 == None):
        titulo = "Algoritmo por " + str(opcion1)
    else:
        titulo = "Algoritmo por " + str(opcion1) + " con la opcion de " + str(opcion2)
    pygame.display.set_caption(titulo)
    reloj = pygame.time.Clock()

    BLANCO = (255, 255, 255)
    NEGRO = (0, 0, 0)
    celda_ancho = ancho // 10
    celda_alto = alto // 10

    # Cargar las imágenes que deseas utilizar
    imagen_muro = pygame.image.load("images/1.png")
    imagen_personaje = pygame.image.load("images/2.png")
    imagen_nave = pygame.image.load("images/3.png")
    imagen_enemigo = pygame.image.load("images/4.png")
    imagen_grogu = pygame.image.load("images/5.png")

    def dibujar_matriz(matriz):
        for fila in range(len(matriz)):
            for columna in range(len(matriz[0])):
                if matriz[fila][columna] == 0:  # Posición libre
                    imagen = None
                elif matriz[fila][columna] == 1:  # Muro
                    imagen = pygame.transform.scale(imagen_muro, (celda_ancho, celda_alto))
                elif matriz[fila][columna] == 2:  # Personaje
                    imagen = pygame.transform.scale(imagen_personaje, (celda_ancho, celda_alto))
                elif matriz[fila][columna] == 3:  # Nave
                    imagen = pygame.transform.scale(imagen_nave, (celda_ancho, celda_alto))
                elif matriz[fila][columna] == 4:  # Enemigo
                    imagen = pygame.transform.scale(imagen_enemigo, (celda_ancho, celda_alto))
                elif matriz[fila][columna] == 5:  # grogu
                    imagen = pygame.transform.scale(imagen_grogu, (celda_ancho, celda_alto))
                if imagen:
                    pantalla.blit(imagen, (columna * celda_ancho, fila * celda_alto))


    # Definir la matriz de entorno-----
    matriz_de_elementos = matriz_de_elementos
    matriz_entorno = matriz_de_elementos

    personaje_x, personaje_y = 0, 0
    for fila in range(len(matriz_de_elementos)):
        for columna in range(len(matriz_de_elementos[fila])):
            if matriz_de_elementos[fila][columna] == 2:
                personaje_x, personaje_y = columna, fila
                break
        else:
            continue
        break

    entorno = ruta_final
    lista_secuencia = entorno.split("->")
    movimientos = lista_secuencia

    ejecutando = True
    movimiento_actual = 0

    while ejecutando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False

        if movimiento_actual < len(movimientos):
            movimiento = movimientos[movimiento_actual]
            if movimiento == "Derecha":
                if personaje_x < 9 and matriz_entorno[personaje_y][personaje_x + 1] != 1:  # Verificar límites y muros
                    personaje_x += 1
            elif movimiento == "Izquierda":
                if personaje_x > 0 and matriz_entorno[personaje_y][personaje_x - 1] != 1:
                    personaje_x -= 1
            elif movimiento == "Arriba":
                if personaje_y > 0 and matriz_entorno[personaje_y - 1][personaje_x] != 1:
                    personaje_y -= 1
            elif movimiento == "Abajo":
                if personaje_y < 9 and matriz_entorno[personaje_y + 1][personaje_x] != 1:
                    personaje_y += 1

            movimiento_actual += 1

        pantalla.fill(BLANCO)
        dibujar_matriz(matriz_entorno)
        matriz_entorno[personaje_y][personaje_x] = 2  # Actualizar posición del personaje en la matriz
        pygame.display.flip()
        pygame.time.delay(500)  # Pausa para visualizar el movimiento


    pygame.quit()