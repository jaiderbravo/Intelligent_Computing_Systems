"""
Jugador de tricy
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Retorna el estado inicial del tablero
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Retorna quien es el jugador que debe jugar.
    """
    X_turno = sum(row.count('X') for row in board)
    O_turno = sum(row.count('O') for row in board)
    return 'X' if X_turno <= O_turno else 'O'


def actions(board):
    """
    Retorna el conjunto de todas las acciones posibles (i,j) disponibles en el tablero.
    """
    Acciones = []
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                Acciones.append((i, j))
    return Acciones


def result(board, Accion):
    """
    Retorna el tablero que resulta de hacer la acción (i,j) en el tablero.
    """
    i, j = Accion
    Turno_jugador = player(board)
    if board[i][j] is not None:
        raise Exception("Movimiento inválido")
    else:
        Nuevo_board = [row[:] for row in board]
        Nuevo_board[i][j] = Turno_jugador
        return Nuevo_board


def winner(board):
    """
    Retorna el ganador del juego
    """
    # Comprobamos filas, columnas y diagonales
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] is not None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not None:
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    return None


def terminal(board):
    """
    Retorna True si el juego se acabó y False si continua.
    """
    # El juego termina si hay un ganador o si no quedan movimientos posibles.
    if winner(board) is not None or all(board[i][j] is not None for i in range(3) for j in range(3)):
        return True
    return False


def utility(board):
    """
    Retorna 1 si X ganó el juego, -1 si O ganó, y 0 si empatan.
    """
    Jugador_Ganador = winner(board)
    if Jugador_Ganador == 'X':
        return 1
    elif Jugador_Ganador == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Retorna la acción que optimiza la elección del jugador.
    """
    def max_value(board):
        if terminal(board):
            return utility(board)

        v = float('-inf')
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
        return v

    def min_value(board):
        if terminal(board):
            return utility(board)

        v = float('inf')
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
        return v

    if terminal(board):
        return None

    if player(board) == 'X':
        v = float('-inf')
        Mejor_movimiento = None
        for action in actions(board):
            min_val = min_value(result(board, action))
            if min_val > v:
                v = min_val
                Mejor_movimiento = action
        return Mejor_movimiento
    else:
        v = float('inf')
        Mejor_movimiento = None
        for action in actions(board):
            max_val = max_value(result(board, action))
            if max_val < v:
                v = max_val
                Mejor_movimiento = action
        return Mejor_movimiento