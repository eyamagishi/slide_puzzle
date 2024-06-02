from . import SCREEN_SIZE, TILE_SIZE, FONT_SIZE, FONT, WHITE, BLACK, BACKGROUND_COLOR
import random
import pygame

pygame.init()

def is_solvable(board):
    flat_board = [tile for row in board for tile in row if tile != 0]
    inversions = sum(sum(tile > flat_board[i] for i in range(j, len(flat_board))) for j, tile in enumerate(flat_board))
    return inversions % 2 == 0

def create_solvable_board():
    while True:
        board = list(range(1, 16)) + [0]
        random.shuffle(board)
        board = [board[i * 4:(i + 1) * 4] for i in range(4)]
        if is_solvable(board):
            return board

def find_empty_tile(board):
    for row in range(4):
        for col in range(4):
            if board[row][col] == 0:
                return row, col

def draw_board(screen, board):
    screen.fill(BACKGROUND_COLOR)
    for row in range(4):
        for col in range(4):
            tile = board[row][col]
            if tile != 0:
                rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, WHITE, rect)
                text = FONT.render(str(tile), True, BLACK)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
    pygame.display.flip()

def move_tile(board, empty_tile, row, col):
    empty_row, empty_col = empty_tile
    if 0 <= row < 4 and 0 <= col < 4:
        board[empty_row][empty_col], board[row][col] = board[row][col], board[empty_row][empty_col]
        return (row, col)
    return empty_tile

def is_solved(board):
    solution = list(range(1, 16)) + [0]
    flat_board = [tile for row in board for tile in row]
    return flat_board == solution
