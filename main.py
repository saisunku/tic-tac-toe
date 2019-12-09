#
# Program that is unbeatable at tic-tac-toe
#


class board():
	"""Tic-tac-toe board class"""

	def __init__(self, board_sz):
		"""Initialize with a board of a given size"""
		self.board_sz = board_sz
		self.board = [[None for j in range(board_sz)] for k in range(board_sz)]
		self.cur_player = 0	# Start with player 0


	def print_board(self):
		"""Prints the board in a pretty format"""
	
		# Construct the lines to be printed and store them in a list
		str_print_list = [0 for j in range(self.board_sz)]

		for j in range(self.board_sz):
			str_print = str(j) + ' | '
			# If there is a character, add it to the list. If not add a space.
			for k in range(self.board_sz):
				if self.board[j][k]:
					str_print = ''.join([str_print, str(self.board[j][k]), ' | '])
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
		return [int(x), int(y)]
		
	
	def is_valid_move(self, x, y):
		"""Check if the move at coordinates [x, y] is a valid move.
		   Return True if valid and False if invalid."""

		# Check that the coordinates are not negative
		if x < 0 or y < 0:
			print('Negative coordinates not allowed')
			return False
		# Check that the coordinates are within board size
		if x >= self.board_sz or y >= self.board_sz:
			print('Coordinates outside the board')
			return False
		# Check that there is no character already there
		if self.board[y][x]:
			print('That square is already taken')
			return False

		return True


	def make_move(self, player):	
		"""Update the board with a player's move"""
		char = ''
		if player == 0:
			char = 'O'
		else:
			char = 'X'

		# Get move coordinates
		[x, y] = self.get_move()
		move_valid = self.is_valid_move(x, y)

		# Repeat until they are valid
		while move_valid == False:
			[x, y] = self.get_move()
			move_valid = self.is_valid_move(x, y)

		# Update board
		self.board[y][x] = char

		# Update current player
		self.cur_player = (self.cur_player + 1)%2


	def get_winner(self):
		"""Check for winner and return the winning player's id. Return None if no winner."""

		def return_winner(char_list):
		# Helper function that checks for winner by converting to a set and checking the length of the set
		# Return the player id if there is a winner and None otherwise
			if len(set(char_list)) == 1:
				if char_list[0] == 'O':
					return 0
				elif char_list[0] == 'X':
					return 1
				else:
					return None
			return None

		# Check horizontally
		for j in range(self.board_sz):
			row = self.board[j]
			to_return = return_winner(row)
			if to_return is not None:
				return to_return

		# Check vertically
		for j in range(self.board_sz):
			column = []
			for k in range(self.board_sz):
				column.append(self.board[k][j])
			to_return = return_winner(column)
			if to_return is not None:
				return to_return

		# Check top-left--bottom-right diagonal
		diag = []
		for j in range(self.board_sz):
			diag.append(self.board[j][j])
		to_return = return_winner(diag)
		if to_return is not None:
			return to_return

		# Check top-right--bottom-left diagonal
		diag = []
		for j in range(self.board_sz):
			diag.append(self.board[j][-j-1])
		to_return = return_winner(diag)
		if to_return is not None:
			return to_return

		# No winner
		return None


	def is_full(self):
		"""Check if the board is full"""
		flattened_board = [char for row in self.board for char in row]
		return not None in flattened_board


# Test initialization and printing
# B = board(3)
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
B = board(3)
assert B.get_winner() == None

B.board[2] = ['X', 'X', 'X']
assert B.get_winner() == 1

B = board(3)
B.board[0][0] = 'O'; B.board[0][1] = 'O'; B.board[0][2] = 'O';
assert B.get_winner() == 0

B = board(3)
B.board[0][0] = 'X'; B.board[1][1] = 'X'; B.board[2][2] = 'X';
assert B.get_winner() == 1

B = board(3)
B.board[0][2] = 'O'; B.board[1][1] = 'O'; B.board[2][0] = 'O';
assert B.get_winner() == 0



# Start playing
sz = int(input('Enter board size you want to play on:  '))
B = board(sz)

is_full = B.is_full()
winner = B.get_winner()

while not is_full and winner is None:
	B.print_board()
	print('Player ' + str(B.cur_player))
	B.make_move(B.cur_player)

	is_full = B.is_full()
	winner = B.get_winner()

print('')
if is_full:
	print('Game ended in draw! Final board position:')
if winner == 0:
	print('Game ended! Player 0 won! Final board position:')
elif winner == 1:
	print('Game ended! Player 1 won! Final board position:')

B.print_board()
