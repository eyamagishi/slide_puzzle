from . import SCREEN_SIZE, TILE_SIZE, FONT_SIZE, FONT, WHITE, BLACK, BACKGROUND_COLOR
from .game_logic import create_board, find_empty_tile, draw_board, move_tile
import pygame
import sys

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

# ゲーム画面の作成
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Number Puzzle")

# ゲーム盤の初期化
board = create_board()
empty_tile = find_empty_tile(board)

# メインループ
def main():
    global empty_tile
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_UP:
                    empty_tile = move_tile(board, empty_tile, empty_tile[0] - 1, empty_tile[1])
                elif event.key == pygame.K_DOWN:
                    empty_tile = move_tile(board, empty_tile, empty_tile[0] + 1, empty_tile[1])
                elif event.key == pygame.K_LEFT:
                    empty_tile = move_tile(board, empty_tile, empty_tile[0], empty_tile[1] - 1)
                elif event.key == pygame.K_RIGHT:
                    empty_tile = move_tile(board, empty_tile, empty_tile[0], empty_tile[1] + 1)
        
        draw_board(screen, board)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
