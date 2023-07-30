class TicTacToe:
	def __init__(self):
		self.board = []

	def create_board(self):
		for i in range(3):
			row = []
			for j in range(3):
				row.append('-')
				self.board.append(row)

	def get_move(player):
		while True:
			try:
				row = int(input(f"Player {player}, enter row number (0, 1, or 2): "))
				col = int(input(f"Player {player}, enter column number (0, 1, or 2): "))
				if 0 <= row < 3 and 0 <= col < 3:
					return row, col
				else:
					print("Invalid input! Row and column should be between 0 and 2.")
			except ValueError:
				print("Invalid input! Please enter numbers for row and column.")

	def make_move(board, player, row, col):
		if board[row][col] == ' ':
			board[row][col] = player
			return True

		return False
