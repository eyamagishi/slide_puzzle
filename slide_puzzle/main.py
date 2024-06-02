from . import SCREEN_SIZE, TILE_SIZE, FONT_SIZE, FONT, WHITE, BLACK, BACKGROUND_COLOR
from .game_logic import create_solvable_board, find_empty_tile, draw_board, move_tile, is_solved
import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("Number Puzzle")

board = create_solvable_board()
empty_tile = find_empty_tile(board)

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
        if is_solved(board):
            print("Congratulations! You solved the puzzle!")
            running = False

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
