import unittest
from slide_puzzle.game_logic import create_board, find_empty_tile, move_tile

class TestGameLogic(unittest.TestCase):
    def test_create_board(self):
        board = create_board()
        self.assertEqual(len(board), 4)
        self.assertTrue(all(len(row) == 4 for row in board))
        flat_board = [tile for row in board for tile in row]
        self.assertCountEqual(flat_board, list(range(16)))

    def test_find_empty_tile(self):
        board = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 0]]
        empty_tile = find_empty_tile(board)
        self.assertEqual(empty_tile, (3, 3))

    def test_move_tile(self):
        board = [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 0]]
        empty_tile = (3, 3)
        empty_tile = move_tile(board, empty_tile, 3, 2)
        self.assertEqual(board[3][3], 15)
        self.assertEqual(board[3][2], 0)
        self.assertEqual(empty_tile, (3, 2))

if __name__ == '__main__':
    unittest.main()
