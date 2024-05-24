from Nodo import Nodo 
import parteGrafica as PG

#No olvidar definir la profundidad dependiendo de el nivel de dificultad escogido
def minimax(nodo, profundidad, jugador_max):
    if (profundidad ==0 or nodo.es_terminal()):
        nodo.utilidad = nodo.evaluar()
        return nodo.utilidad
    
    if (jugador_max):
        max_evaluacion = float('-inf')
        
        # Para cada movimiento valido del Yoshi que tiene el turno
        for move in PG.get_knight_moves(nodo.yoshi_positions[nodo.turno]):
            posiciones_nuevas = list(nodo.yoshi_positions)
            posiciones_nuevas[nodo.turn] = move #Cambio la posicion para el jugador con el turno
            nodo_hijo = Nodo(posiciones_nuevas, 1 - nodo.turno, nodo.profundidad +1, nodo)
            nodo.guardar_hijo(nodo_hijo)
            eval = minimax(nodo_hijo, profundidad - 1, False)
            max_evaluacion = max(max_evaluacion, eval)
        nodo.utilidad = max_evaluacion
        return max_evaluacion

    else:
        min_evaluacion = float('inf')

        # Para cada movimiento valido del Yoshi que tiene el turno
        for move in PG.get_knight_moves(nodo.yoshi_positions[nodo.turno]):
            posiciones_nuevas = list(nodo.yoshi_positions)
            posiciones_nuevas[nodo.turn] = move #Cambio la posicion para el jugador con el turno
            nodo_hijo = Nodo(posiciones_nuevas, 1 - nodo.turno, nodo.profundidad +1, nodo)
            nodo.guardar_hijo(nodo_hijo)
            eval = minimax(nodo_hijo, profundidad - 1, True)
            min_evaluacion = min(min_evaluacion, eval)
        nodo.utilidad = min_evaluacion
        return min_evaluacion
     
def mejor_movimiento(yoshi_positions, turno, profundidad):

    #Defino la raiz del arbol
    raiz = Nodo(yoshi_positions, turno, 0)
    mejor_evaluacion = float('-inf') if turno == 0 else float('inf') 
    mejor_movimiento = None

    for movimiento in PG.get_knight_moves(yoshi_positions[turno]):
        nuevas_posiciones = list(nuevas_posiciones)
        nuevas_posiciones[turno]= movimiento
        nodo_hijo = Nodo(nuevas_posiciones, 1 - turno, 1, raiz)
        raiz.guardar_hijo(nodo_hijo) 
        eval = minimax(nodo_hijo, profundidad -1, turno == 1)
        
        if(turno == 0 and eval> mejor_evaluacion) or (turno ==1 and eval< mejor_evaluacion):
            mejor_evaluacion = eval 
            mejor_movimiento = movimiento
            
    return mejor_movimiento 

