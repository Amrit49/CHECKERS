from copy import deepcopy
import pygame

RED = (157, 192, 139)
BlACK = (237, 241, 214)


def minimaxab(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position

    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves(position, BlACK, game):
            evaluation = minimaxab(move, depth - 1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves(position, RED, game):
            evaluation = minimaxab(move, depth - 1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move
# def minimaxab(board, player, depth, alpha, beta):
#     best_move = None
#     if depth == 0 or board.winner() != None:
#         return board.evaluate(), board
#     if player == 1:
#         best = float('-inf')
#         for move in get_all_moves(board, BlACK):
#             val = minimaxab(move, -1, depth-1, alpha, beta)[0]
#             if val > best:
#                 best = val
#                 best_move = move
#                 # print(val)
#                 # print(board)
#                 alpha = max(alpha, best)
#                 if alpha >= beta:
#                     break
#         return best, best_move
#     else:
#         best = float('inf')
#         for move in get_all_moves(board, BlACK):
#                 val = minimaxab(move, 1, depth -1, alpha, beta)[0]
#                 if val < best:
#                     best = val
#                     best_move = move
#                 # print(val)
#                 # print(board)
#                 beta = min(beta, best)
#                 if alpha >= beta:
#                     break
#         return best, best_move

def simulate_move(piece, move, board, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            # draw_moves(game, board, piece)
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, skip)
            moves.append(new_board)

    return moves


def draw_moves(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.screen)
    pygame.draw.circle(game.screen, (0, 255, 0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()