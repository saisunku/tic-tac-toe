#
# Tests for individual functions in the tic-tac-toe module
#

from tic_tac_toe import tic_tac_toe


# Test initialization and printing
B = tic_tac_toe(3)
print(B.board)

# B.board[2][2] = 'X'
B.board[0][0] = 'O'
B.print_board()

# Test get_move
print(B.get_move())

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



