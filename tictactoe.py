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
	
	def evaluate(self, board, player1, player2):
		if self.check_win(board, player1):
			return 1
		elif self.check_win(board, player2):
			return -1
		else:
			return 0

	def minimax(self, board, depth, is_maximizing, player1, player2, max_depth):
		if depth >= max_depth:
			return 0

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
						score = self.minimax(board, depth + 1, False, player1, player2, max_depth)
						board[i][j] = ' '
						best_score = max(score, best_score)
			return best_score
		else:
			best_score = math.inf
			for i in range(3):
				for j in range(3):
					if board[i][j] == ' ':
						board[i][j] = player2
						score = self.minimax(board, depth + 1, True, player1, player2, max_depth)
						board[i][j] = ' '
						best_score = min(score, best_score)
			return best_score

	def get_best_move(self, board, player1, player2, difficulty):
		# Easy level: limit the AI's search space to a depth of 1
		if difficulty == 'easy':
			max_depth = 1
		# Hard level: allow the AI to search more moves ahead
		elif difficulty == 'hard':
			max_depth = 5
		else:
			raise ValueError("Invalid difficulty level!")

		best_score = -math.inf
		best_move = None

		for i in range(3):
			for j in range(3):
				if board[i][j] == ' ':
					board[i][j] = player1
					score = self.minimax(board, 0, False, player1, player2, max_depth)
					board[i][j] = ' '

					if score > best_score:
						best_score = score
						best_move = (i, j)

		return best_move

	def print_stats(self, wins, losses, ties):
		print("========== Statistics ==========")
		print(f"Wins: {wins}")
		print(f"Losses: {losses}")
		print(f"Ties: {ties}")
		print("===============================")

	def tic_tac_toe_game(self):
		player1 = 'X'
		player2 = 'O'
		ai_player = player2
		wins = 0
		losses = 0
		ties = 0

		while True:
			board = self.create_board()
			current_player = player1

			# Ask user if they want to play against the AI
			vs_ai = input("Do you want to play against the AI? (yes/no): ")
			if vs_ai.lower() == 'no':
				ai_player = None

			# Ask user to choose difficulty level if playing against the AI
			if ai_player:
				difficulty = input("Choose AI difficulty (easy/hard): ")
				if difficulty.lower() not in ('easy', 'hard'):
					print("Invalid difficulty level. Defaulting to hard.")
					difficulty = 'hard'
			else:
				difficulty = None

			while not self.is_game_over(board, current_player):
				self.display_board(board)

				if current_player == ai_player:
					row, col = self.get_best_move(board, player1, player2, difficulty)
					self.make_move(board, current_player, row, col)
					print(f"AI plays at row {row}, column {col}.")
				else:
					row, col = self.get_move(current_player)

					if not self.make_move(board, current_player, row, col):
						print("Cell already taken. Try again.")
						continue

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
				if winner == 'X':
					wins += 1
				else:
					losses += 1
			else:
				print("It's a tie!")
				ties += 1

			self.print_stats(wins, losses, ties)

			else:
				print("It's a tie!")

			if not self.play_again():
				break

if __name__ == "__main__":
	game = TicTacToe()
	game.tic_tac_toe_game()
