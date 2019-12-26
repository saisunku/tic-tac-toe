#
# Script that starts a game of tic-tac-toe
#

import tic-tac-toe


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
