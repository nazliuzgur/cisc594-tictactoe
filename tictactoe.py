import math

class TicTacToe:
	def create_board(self):
		return [[' ' for _ in range(3)] for _ in range(3)]

	def display_board(self, board):
		for row in board:
			print("|".join(row))
			print("-----")

	def get_move(self, player):
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

	def make_move(self, board, player, row, col):
		if board[row][col] == ' ':
			board[row][col] = player
			return True

		return False

	def check_win(self, board, player):
		for row in board:
			if all(cell == player for cell in row):
				return True

		for col in range(3):
			if all(board[row][col] == player for row in range(3)):
				return True

		if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
			return True

		return False

	def check_tie(self, board):
		for row in board:
			if ' ' in row:
				return False
		return True

	def is_game_over(self, board, player):
		return self.check_win(board, player) or self.check_tie(board)

	def get_winner(self, board, player1, player2):
		if self.check_win(board, player1):
			return player1
		elif self.check_win(board, player2):
			return player2
		else:
			return None

	def play_again(self):
		response = input("Do you want to play again? (yes/no): ")
		return response.lower() == 'yes'

	def reset_board(self, board):
		for i in range(3):
			for j in range(3):
				board[i][j] = ' '

	def tic_tac_toe_game(self):
		player1 = 'X'
		player2 = 'O'

		while True:
			board = self.create_board()
			current_player = player1

			while not self.is_game_over(board, current_player):
				self.display_board(board)
				row, col = self.get_move(current_player)

				if not self.make_move(board, current_player, row, col):
					print("Cell already taken. Try again.")
					continue

				current_player = player2 if current_player == player1 else player1

			self.display_board(board)

			winner = self.get_winner(board, player1, player2)
			if winner:
				print(f"Player {winner} wins!")
			else:
				print("It's a tie!")

			if not self.play_again():
				break
	
	def evaluate(self, board, player1, player2):
		if self.check_win(board, player1):
			return 1
		elif self.check_win(board, player2):
			return -1
		else:
			return 0

	def minimax(self, board, depth, is_maximizing, player1, player2):
		if self.check_win(board, player1):
			return 1
		elif self.check_win(board, player2):
			return -1
		elif self.check_tie(board):
			return 0

		if is_maximizing:
			best_score = -math.inf
			for i in range(3):
				for j in range(3):
					if board[i][j] == ' ':
						board[i][j] = player1
						score = self.minimax(board, depth + 1, False, player1, player2)
						board[i][j] = ' '
						best_score = max(score, best_score)
			return best_score
		else:
			best_score = math.inf
			for i in range(3):
				for j in range(3):
					if board[i][j] == ' ':
						board[i][j] = player2
						score = self.minimax(board, depth + 1, True, player1, player2)
						board[i][j] = ' '
						best_score = min(score, best_score)
			return best_score

	def get_best_move(self, board, player1, player2):
		best_score = -math.inf
		best_move = None

		for i in range(3):
			for j in range(3):
				if board[i][j] == ' ':
					board[i][j] = player1
					score = self.minimax(board, 0, False, player1, player2)
					board[i][j] = ' '

					if score > best_score:
						best_score = score
						best_move = (i, j)

		return best_move

if __name__ == "__main__":
	game = TicTacToe()
	game.tic_tac_toe_game()
