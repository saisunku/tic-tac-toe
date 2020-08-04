#
# Tests for individual functions in the tic-tac-toe module using the pytest module
#

from tic_tac_toe import tic_tac_toe

# # Test initialization and printing
# B = tic_tac_toe(3)
# print(B.board)

# # B.board[2][2] = 'X'
# B.board[0][0] = 'O'
# B.print_board()

# # Test get_move
# print(B.get_move())

# Test get_winner
def test_get_winner_1():
    B = tic_tac_toe(3)
    assert B.get_winner() == None

def test_get_winner_2():
    B.board[2] = ['X', 'X', 'X']
    assert B.get_winner() == 'X'

def test_get_winner_3():
    B = tic_tac_toe(3)
    B.board[0][0] = 'O'; B.board[0][1] = 'O'; B.board[0][2] = 'O'
    assert B.get_winner() == 'O'

def test_get_winner_4():
    B = tic_tac_toe(3)
    B.board[0][0] = 'X'; B.board[1][1] = 'X'; B.board[2][2] = 'X'
    assert B.get_winner() == 'X'

def test_get_winner_5():
    B = tic_tac_toe(3)
    B.board[0][2] = 'O'; B.board[1][1] = 'O'; B.board[2][0] = 'O'
    assert B.get_winner() == 'O'

# Test random_ai
B = tic_tac_toe(3, ai_player = 'X')
B.board = [['O', None, None], [None, 'O', None], [None, None, 'O']]

def test_random_ai_1():
    random_move = B.random_ai('X')
    assert random_move not in ([0, 0], [1, 1], [2, 2])

def test_random_ai_2():
    random_move = B.random_ai('O')
    assert random_move not in ([0, 0], [1, 1], [2, 2])

# Test minimax scoring
def test_minimax_score_1():
    B.board = [['X', 'X', 'X'], [None, None, None], [None, None, None]]
    assert B.get_minimax_score(B.board, 'X') == (10, None)

def test_minimax_score_2():
    B.board = [['O', 'O', 'O'], [None, None, None], [None, None, None]]
    assert B.get_minimax_score(B.board, 'X') == (-10, None)

def test_minimax_score_3():
    B.board = [['O', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]
    assert B.get_minimax_score(B.board, 'X') == (0, None)

def test_minimax_score_4():
    B.board = [['O', 'X', 'O'], ['X', 'X', None], [None, 'O', None]]
    assert B.get_minimax_score(B.board, 'X') == (10, [2, 1])

def test_minimax_score_5():
    B.board = [['O', 'X', 'O'], ['O', None, 'X'], [None, 'O', None]]
    assert B.get_minimax_score(B.board, 'X')[0] == 0

def test_minimax_score_6():
    B.board = [['O', 'X', 'O'], ['X', 'X', None], ['X', 'O', None]]
    assert B.get_minimax_score(B.board, 'O')[0] == 0

def test_minimax_score_7():
    B.board = [['O', None, None], [None, 'O', None], ['X', 'X', None]]
    assert B.get_minimax_score(B.board, 'X') == (10, [2, 2])

# Test minimax
def test_minimax_1():
    B.board = [['O', None, 'X'], [None, 'O', 'X'], [None, None, None]]
    assert B.minimax('X') == [2, 2]
def test_minimax_2():
    B.board = [['O', 'O', None], [None, 'X', None], [None, None, None]]
    assert B.minimax('X') == [2, 0]
