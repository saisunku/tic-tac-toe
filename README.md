# tic-tac-toe

A program that plays tic-tac-toe on an arbitrarily sized board using the Minimax algorithm

Based on Robert Heaton's website https://robertheaton.com/2018/10/09/programming-projects-for-advanced-beginners-3-a/

## Contents
  - `tic_tac_toe.py` - Module containing the `tic_tac_toe` class
	  - There are three different players
		-  Human, which gets the move from the keyboard
		- Random, which randomly selects from one of the available squares
		- Minimax, which uses the Minimax algorithm
		  - Minimax algorithm includes caching and some pruning to improve speed
  - `tests.py` are some tests for individual functions in the `tic_tac_toe` class
  - `main.py` runs a human vs computer (either Random or Minimax) game

Even with caching and pruning, Minimax takes an unreasonably long time for board sizes greater than 3.
