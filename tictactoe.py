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

	def check_win(board, player):
		for row in board:
			if all(cell == player for cell in row):
				return True

		for col in range(3):
			if all(board[row][col] == player for row in range(3)):
				return True

		if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
			return True

		return False

	def check_tie(board):
		for row in board:
			if ' ' in row:
				return False
		return True

	def is_game_over(board, player):
		return self.check_win(board, player) or self.check_tie(board)

	def get_winner(board, player1, player2):
		if check_win(board, player1):
			return player1
		elif check_win(board, player2):
			return player2
		else:
			return None
