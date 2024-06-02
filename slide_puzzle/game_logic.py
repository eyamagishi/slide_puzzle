from . import SCREEN_SIZE, TILE_SIZE, FONT_SIZE, FONT, WHITE, BLACK, BACKGROUND_COLOR
import random
import pygame

# Pygameの初期化
pygame.init()

# 定数の設定
SCREEN_SIZE = 400
TILE_SIZE = SCREEN_SIZE // 4
FONT_SIZE = 48
FONT = pygame.font.SysFont(None, FONT_SIZE)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND_COLOR = (30, 30, 30)

def create_board():
    board = list(range(1, 16)) + [0]
    random.shuffle(board)
    return [board[i * 4:(i + 1) * 4] for i in range(4)]

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
