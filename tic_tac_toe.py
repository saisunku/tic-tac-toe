#
# Program that is unbeatable at tic-tac-toe using the minimax algorithm
#

import random
import copy

class tic_tac_toe():
	"""Tic-tac-toe board class"""

	def __init__(self, board_sz, ai_player = None):
		"""Initialize with a board of a given size and the character of the AI player if there is one"""
		self.board_sz = board_sz
		self.board = [[None for j in range(board_sz)] for k in range(board_sz)]
		self.cur_player = 'O'	# Start with player 'O'
		self.ai_player = ai_player
		self.minimax_cache = {}


	def print_board(self, board = None):
		"""Prints the board in a pretty format"""
	
		if board == None:
			board = self.board

		# Construct the lines to be printed and store them in a list
		str_print_list = [0 for j in range(self.board_sz)]

		for j in range(self.board_sz):
			str_print = str(j) + ' | '
			# If there is a character, add it to the list. If not add a space.
			for k in range(self.board_sz):
				if board[j][k]:
					str_print = ''.join([str_print, str(board[j][k]), ' | '])
				else:
					str_print += '  | '

			str_print += ' '
			str_print_list[j] = str_print

		# Construct the header
		header = '    '
		for j in range(self.board_sz):
			header = ''.join([header, str(j), '   '])

		# Construct the spacer line
		spacer = '-'*(self.board_sz*5 + 2)
	
		# Print
		print('')
		print(header)
		print(spacer)
		for j in range(self.board_sz):
			print(str_print_list[j])
			print(spacer)
		print('')


	def get_move(self):
		"""Get X and Y coordinates of the player's move"""

		x = input("Enter X coordinate of your move:  ")
		y = input("Enter Y coordinate of your move:  ")
		try:
			x = int(x)
			y = int(y)
		except:
			x = -1
			y = -1

		return [x, y]
		
	
	def is_valid_move(self, x, y):
		"""Check if the move at coordinates [x, y] is a valid move.
		   Return True if valid and False if invalid."""

		# Check that the coordinates are not negative or outside the board size
		if x < 0 or y < 0 or x >= self.board_sz or y >= self.board_sz:
			print('Coordinates not allowed')
			return False
		# Check that there is no character already there
		if self.board[y][x]:
			print('That square is already taken')
			return False

		return True


	def make_move(self, player, x, y):	
		"""Update the board with a player's move. Does not check for move validity."""

		# Update board
		self.board[y][x] = player

		# Update current player
		if self.cur_player == 'O':
			self.cur_player = 'X'
		else:
			self.cur_player = 'O'


	def make_move_minimax(self, board, player, x, y):
		"""Function that copies, updates and returns a new board. Needed for Minimax."""

		new_board = copy.deepcopy(board)
		new_board[y][x] = player
		return new_board


	def get_winner(self, board = None):
		"""Check for winner and return the winning player's id. Return None if no winner.
		   If no board is provided, use the game board."""

		if board == None:
			board = self.board

		def return_winner(char_list):
		# Helper function that checks for winner by converting to a set and checking the length of the set
		# Return the player id if there is a winner and None otherwise
			if len(set(char_list)) == 1:
				return char_list[0]
			else:
				return None

		possible_winners = []

		# Check horizontally
		for j in range(self.board_sz):
			row = board[j]
			possible_winners.append(row)

		# Check vertically
		for j in range(self.board_sz):
			column = []
			for k in range(self.board_sz):
				column.append(board[k][j])
			possible_winners.append(column)

		# Check top-left--bottom-right diagonal
		diag = []
		for j in range(self.board_sz):
			diag.append(board[j][j])
		possible_winners.append(diag)

		# Check top-right--bottom-left diagonal
		diag = []
		for j in range(self.board_sz):
			diag.append(board[j][-j-1])
		possible_winners.append(diag)

		for pos_winner in possible_winners:
			winner = return_winner(pos_winner)
			if winner: return winner

		# No winner
		return None


	def is_full(self, board = None):
		"""Check if the board is full. If no board is given, use the game board"""
		if board == None:
			board = self.board

		flattened_board = [char for row in board for char in row]
		return not None in flattened_board


	def board_to_tuple(self, board):
		"""Convert the given board, which is a list, to a tuple so that it can be hashed"""
		return tuple(tuple(row) for row in board)


	def get_sym_equiv(self, board):
		"""Return a list of all boards that are symmetry-equivalent versions of the current board 
		   including the current board"""
		
		sym_list = [board]

		# There are six symmetry operations on a square: ROT90, ROT180, ROT270,
		# MIR_VERT, MIR_HORIZ, MIR_DIAG (main diagonal), MIR_DIAG2 (other diagonal)

		# MIR_VERT
		MIR_VERT = [[None for j in range(self.board_sz)] for k in range(self.board_sz)]
		for j in range(len(board)):
			MIR_VERT[j] = board[-j-1]

		sym_list.append(MIR_VERT)


		# MIR_HORIZ
		MIR_HORIZ = [[None for j in range(self.board_sz)] for k in range(self.board_sz)]
		for j in range(len(board)):
			for k in range(len(board)):
				MIR_HORIZ[j][k] = board[j][-k-1]

		sym_list.append(MIR_HORIZ)
			

		# MIR_DIAG (main diagonal)
		MIR_DIAG = [[None for j in range(self.board_sz)] for k in range(self.board_sz)]
		for j in range(len(board)):
			for k in range(len(board)):
				MIR_DIAG[j][k] = board[k][j]

		sym_list.append(MIR_DIAG)
		
	
		# MIR_DIAG2 (other diagonal)
		MIR_DIAG2 = [[None for j in range(self.board_sz)] for k in range(self.board_sz)]
		for j in range(len(board)):
			for k in range(len(board)):
				MIR_DIAG2[j][k] = board[-k-1][-j-1]

		sym_list.append(MIR_DIAG2)
		

		# ROT90
		ROT90 = [[None for j in range(self.board_sz)] for k in range(self.board_sz)]
		for j in range(len(board)):
			for k in range(len(board)):
				ROT90[k][-j-1] = board[j][k]

		sym_list.append(ROT90)
	

		# ROT180
		ROT180 = [[None for j in range(self.board_sz)] for k in range(self.board_sz)]
		for j in range(len(board)):
			for k in range(len(board)):
				ROT180[k][-j-1] = ROT90[j][k]

		sym_list.append(ROT180)
	

		# ROT270
		ROT270 = [[None for j in range(self.board_sz)] for k in range(self.board_sz)]
		for j in range(len(board)):
			for k in range(len(board)):
				ROT270[k][-j-1] = ROT180[j][k]

		sym_list.append(ROT270)
	

		# Check that four rotations give back the original board
		# ROT360 = [[None for j in range(self.board_sz)] for k in range(self.board_sz)]
		#
		# for j in range(len(board)):
		#	for k in range(len(board)):
		#		ROT360[k][-j-1] = ROT270[j][k]
		#
		# assert ROT360 == board
		
		return sym_list


	
	### Player functions ###

	def human_player(self, player):
		"""Prompt the human player to provide the coordinates for the next move"""
		# Get move coordinates
		[x, y] = self.get_move()
		move_valid = self.is_valid_move(x, y)

		# Repeat until they are valid
		while move_valid == False:
			[x, y] = self.get_move()
			move_valid = self.is_valid_move(x, y)

		return [x, y]


	def random_ai(self, player):
		"""Randomly select and return the coordinates of an available square"""

		flattened_board = [char for row in self.board for char in row]
		avail_sqr = [idx for (idx, sqr) in enumerate(flattened_board) if not sqr]
	
		rand_idx = random.randrange(len(avail_sqr))
		rand_sqr = avail_sqr[rand_idx]	# Index of the chosen square

		# Convert to x, y coordinates
		y = rand_sqr//self.board_sz
		x = rand_sqr%self.board_sz

		return [x, y]


	def get_minimax_score(self, board, player):
		"""Returns the minimax score and the best move for a given board position and player"""
		
		# If there is a winner return the score
		winner = self.get_winner(board)
		if winner:
			if winner == self.ai_player: 
				return 10, None
			else:
				return -10, None

		# If board is full and there is no winner, it's a draw
		if self.is_full(board):
			return 0, None

		# No winner and not a draw, so get all legal moves which is all the empty squares
		moves = [[x, y] for x in range(self.board_sz) for y in range(self.board_sz) if not board[y][x]]

		# Get scores for all the moves
		scores = []
		for move in moves:
			new_board = self.make_move_minimax(board, player, move[0], move[1])

			opponent = ''
			if player == 'X':
				opponent = 'O'
			else:
				opponent = 'X'
			
			# Check if board or its symmetry equivalent boards is in cache
			sym_list = self.get_sym_equiv(new_board)

			for sym_board in sym_list:
				if self.board_to_tuple(sym_board) in self.minimax_cache:
					score = self.minimax_cache[self.board_to_tuple(sym_board)]
					scores.append(score)
					break

			# If not, calculate the score and add new board and its symmetry-equivalents to cache
			else:
				score = self.get_minimax_score(new_board, opponent)[0]
				scores.append(score)
				for sym_board in sym_list:
					self.minimax_cache[self.board_to_tuple(sym_board)] = scores[-1]

			# If the maximizing player gets a win or the minimizing player gets a win,
			# we can stop evaluating the rest of the moves
			if player == self.ai_player and score == 10:
				break
			if opponent == self.ai_player and score == -10:
				break

		if player == self.ai_player:
			return max(scores), moves[scores.index(max(scores))]
		else:
			return min(scores), moves[scores.index(min(scores))]


	def minimax(self, player):
		"""Wrapper function for get_minimax_score which returns the best move"""

		_, best_move = self.get_minimax_score(self.board, player)

		return best_move
