import unittest
from tic_tac_toe import TicTacToe

class TestTicTacToeVersion1(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_board_creation(self):
        board = self.game.create_board()
        expected_board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertEqual(board, expected_board)

    def test_player_moves(self):
        board = self.game.create_board()
        self.game.make_move(board, 'X', 0, 0)
        self.assertEqual(board[0][0], 'X')

    def test_ai_moves(self):
        board = self.game.create_board()
        # Simulate AI's move on 'easy' difficulty
        row, col = self.game.get_best_move(board, 'X', 'O', 'easy')
        # Verify AI's move is within valid range
        self.assertGreaterEqual(row, 0)
        self.assertLess(row, 3)
        self.assertGreaterEqual(col, 0)
        self.assertLess(col, 3)

        # Verify AI's move is an empty cell
        self.assertEqual(board[row][col], ' ')

        # Simulate AI's move on 'hard' difficulty
        row, col = self.game.get_best_move(board, 'X', 'O', 'hard')
            
        # Verify AI's move is within valid range
        self.assertGreaterEqual(row, 0)
        self.assertLess(row, 3)
        self.assertGreaterEqual(col, 0)
        self.assertLess(col, 3)

        # Verify AI's move is an empty cell
        self.assertEqual(board[row][col], ' ')

if __name__ == '__main__':
    unittest.main()
