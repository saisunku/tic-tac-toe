#
# Program that is unbeatable at tic-tac-toe
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

		# Check horizontally
		for j in range(self.board_sz):
			row = board[j]
			to_return = return_winner(row)
			if to_return is not None:
				return to_return

		# Check vertically
		for j in range(self.board_sz):
			column = []
			for k in range(self.board_sz):
				column.append(board[k][j])
			to_return = return_winner(column)
			if to_return is not None:
				return to_return

		# Check top-left--bottom-right diagonal
		diag = []
		for j in range(self.board_sz):
			diag.append(board[j][j])
		to_return = return_winner(diag)
		if to_return is not None:
			return to_return

		# Check top-right--bottom-left diagonal
		diag = []
		for j in range(self.board_sz):
			diag.append(board[j][-j-1])
		to_return = return_winner(diag)
		if to_return is not None:
			return to_return

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
		avail_sqr = []	# List that contains the indices of available squares
		for idx, sqr in enumerate(flattened_board):
			if sqr == None:
				avail_sqr.append(idx)
		
		rand_idx = random.randrange(len(avail_sqr))
		rand_sqr = avail_sqr[rand_idx]	# Index of the chosen square

		# Convert to x, y coordinates
		y = rand_sqr//self.board_sz
		x = rand_sqr%self.board_sz

		return [x, y]


	def get_minimax_score(self, board, player):
		"""Returns the minimax score for the given board position for the given player"""
		
		# If there is a winner return the score
		winner = self.get_winner(board)
		if winner is not None:
			if winner == self.ai_player: 
				return 10
			else:
				return -10

		# If board is full and there is no winner, it's a draw
		if self.is_full(board):
			return 0

		# No winner and not a draw, so get all legal moves which is all the empty squares
		moves = []
		for x in range(self.board_sz):
			for y in range(self.board_sz):
				if board[y][x] == None:
					moves.append([x, y])

		# Get scores for all the moves
		scores = []
		for move in moves:
			new_board = self.make_move_minimax(board, player, move[0], move[1])
			# self.print_board(new_board)

			opponent = ''
			if player == 'X':
				opponent = 'O'
			else:
				opponent = 'X'

			score = self.get_minimax_score(new_board, opponent)
			scores.append(score)

			# If the maximizing player gets a win or the minimizing player gets a win,
			# we can stop evaluating the rest of the moves
			if player == self.ai_player and score == 10:
				break
			if opponent == self.ai_player and score == -10:
				break

		if player == self.ai_player:
			return max(scores)
		else:
			return min(scores)


	def minimax(self, player):
		"""Minimax algorithm for tic-tac-toe"""

		# Get valid moves from the game board
		moves = []
		for x in range(self.board_sz):
			for y in range(self.board_sz):
				if self.board[y][x] == None:
					moves.append([x, y])

		# Make each move and calculate score
		scores = [0 for j in range(len(moves))]
		if player == 'X':
			opponent = 'O'
		else:
			opponent = 'X'

		for idx, move in enumerate(moves):
			new_board = self.make_move_minimax(self.board, player, move[0], move[1])

			# Check if board or its symmetry equivalent boards is in cache
			sym_list = self.get_sym_equiv(new_board)

			for sym_board in sym_list:
				if self.board_to_tuple(sym_board) in self.minimax_cache:
					scores[idx] = self.minimax_cache[self.board_to_tuple(sym_board)]
					break

			# If not, calculate the score and add new board and its symmetry-equivalents to cache
			else:
				scores[idx] = self.get_minimax_score(new_board, opponent)
				for sym_board in sym_list:
					self.minimax_cache[self.board_to_tuple(sym_board)] = scores[idx]

		# Find the move with the highest score
		best_move_idx = scores.index(max(scores))
		
		return moves[best_move_idx]



# Test initialization and printing
# B = tic_tac_toe(3)
# print(B.board)

# B.board[2][2] = 'X'
# B.board[0][0] = 'O'
# B.print_board()

# Test get_move and make_move
# print(B.get_move())

# B.make_move(0)
# B.print_board()
# B.make_move(1)
# B.print_board()


# Test get_winner
B = tic_tac_toe(3)
assert B.get_winner() == None

B.board[2] = ['X', 'X', 'X']
assert B.get_winner() == 'X'

B = tic_tac_toe(3)
B.board[0][0] = 'O'; B.board[0][1] = 'O'; B.board[0][2] = 'O';
assert B.get_winner() == 'O'

B = tic_tac_toe(3)
B.board[0][0] = 'X'; B.board[1][1] = 'X'; B.board[2][2] = 'X';
assert B.get_winner() == 'X'

B = tic_tac_toe(3)
B.board[0][2] = 'O'; B.board[1][1] = 'O'; B.board[2][0] = 'O';
assert B.get_winner() == 'O'


# Test minimax scoring
B = tic_tac_toe(3, ai_player = 'X')
B.board = [['X', 'X', 'X'], [None, None, None], [None, None, None]]
assert B.get_minimax_score(B.board, 'X') == 10

B.board = [['O', 'O', 'O'], [None, None, None], [None, None, None]]
assert B.get_minimax_score(B.board, 'X') == -10

B.board = [['O', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
assert B.get_minimax_score(B.board, 'X') == 0

B.board = [['O', 'X', 'O'], ['X', 'X', None], [None, None, None]]
assert B.get_minimax_score(B.board, 'X') == 10

B.board = [['O', 'X', 'O'], ['O', None, 'X'], [None, 'O', None]]
assert B.get_minimax_score(B.board, 'X') == 0

B.board = [['O', 'X', 'O'], ['X', 'X', None], ['X', 'O', None]]
assert B.get_minimax_score(B.board, 'O') == 0

B.board = [['O', None, None], [None, 'O', None], ['X', 'X', None]]
assert B.get_minimax_score(B.board, 'X') == 10




# Test minimax
B.board = [['O', None, 'X'], [None, 'O', 'X'], [None, None, None]]
assert B.minimax('X') == [2, 2]

B.board = [['O', 'O', None], [None, 'X', None], [None, None, None]]
assert B.minimax('X') == [2, 0]



# Start playing
sz = int(input('Enter board size you want to play on:  '))

ai_opponent = ''
while ai_opponent not in ['R', 'M']:
	ai_opponent = input('Choose your AI opponent. R for random AI, M for minimax.  ')

B = tic_tac_toe(sz, ai_player = 'X')

while not B.is_full() and B.get_winner() is None:
	B.print_board()
	print('Player ' + str(B.cur_player))
	if B.cur_player == 'O':
		[x, y] = B.human_player(B.cur_player)
	else:
		if ai_opponent == 'M':
			[x, y] = B.minimax(B.cur_player)
		else:
			[x, y] = B.random_ai(B.cur_player)

	B.make_move(B.cur_player, x, y)

print('')
if B.is_full():
	print('Game ended in draw! Final board position:')
if B.get_winner() == 'O':
	print('Game ended! You won :) Final board position:')
elif B.get_winner() == 'X':
	print('Game ended! AI won :( Final board position:')

B.print_board()
