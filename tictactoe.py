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

	def play_again():
		response = input("Do you want to play again? (yes/no): ")
		return response.lower() == 'yes'

	def reset_board(board):
		for i in range(3):
			for j in range(3):
				board[i][j] = ' '

	def tic_tac_toe_game():
		player1 = 'X'
		player2 = 'O'

		while True:
			board = create_board()
			current_player = player1

			while not is_game_over(board, current_player):
				display_board(board)
				row, col = get_move(current_player)

				if not make_move(board, current_player, row, col):
					print("Cell already taken. Try again.")
					continue

				current_player = player2 if current_player == player1 else player1

		display_board(board)

		winner = get_winner(board, player1, player2)
		if winner:
			print(f"Player {winner} wins!")
		else:
			print("It's a tie!")

		if not play_again():
			break

if __name__ == "__main__":
    tic_tac_toe_game()
