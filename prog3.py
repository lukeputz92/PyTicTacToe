"""
                                                                    
  Program:     Tic-Tac-Toe NxN                                           
                                                                     
  Author:      Luke Putz
  Email:       lp375410@ohio.edu
                                                                
                                                                    
  Description: This script plays a nxn game of
               Tic Tac Toe with save option                  
                                                                    
  Date:        03/21/17                                                                 
"""
import random, json

"""
    Function: Print_Help()
    Purpose: Prints help diagram of board
    Calls: menu()
"""

def print_help(n):
	print "Help Diagram: "
	print
	count = 0
	for row in range(n):
		print("  " *16),
		for col in range(n):
			print str(row)+str(col),
		print
	print
	menu(n)

"""
    Function: print_board(board)
    Purpose: Prints current state of board
    Calls: none
"""
def print_board(board, n):
	print "Board: "
	for i in range(0,n):
		print("  " *16),
		for j in range(0,n):
			print board[i][j],
		print
	print

"""
    Function: check_rows(board)
    Purpose: checks rows for matches using a set
    		 to determine if all elements are the same
    Calls: none
"""
def check_rows(board):
	for row in board:
		if len(set(row)) == 1:
			return row[0]
	return 0

"""
    Function: check_diagonals(board)
    Purpose: checks diagonals for matches using a set
    		 to determine if all elements are the same
    Calls: none
"""

def check_diagonals(board):
	if len(set([board[i][i] for i in range(len(board))])) == 1:
		return board[0][0]
	if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
		return board[0][len(board)-1]
	return 0

"""
    Function: transpose(board)
    Purpose: returns a copy of the board with rows interchanged with cols
    Calls: none
"""

def transpose(board):
	return [[board[j][i] for j in range(len(board))] for i in range(len(board[0]))]

"""
    Function: who_won()
    Purpose: checks for the 10 winning conditions
             then returns a string x/o or # 
    Calls: none
"""

def who_won(board):
    #transpose the board and then compare
	for newBoard in [board, transpose(board)]:
		result = check_rows(newBoard)
		if result:
			return result
	return check_diagonals(board)

"""
    Function: check_move()
    Purpose: makes sure move is legal
    Calls: none
"""		
def check_move(board, sq, n):
	if len(sq) < 2:
		print 'Move must contain two digits [row][col]'
		return False
	elif int(sq) < 0 or int(sq) > 99:
		return False 
	elif int(sq[0]) > (n-1) or int(sq[1]) > (n-1):
		return False
	elif board[int(sq[0])][int(sq[1])] != '#':
		return False
	else:
		return True

"""
    Function: move
    Purpose: sets square(sq) to marker(x/o) on board
             if check_move is true
    Calls: check_move()
"""

def move(board, sq, marker, n):
	marker = marker.lower()
	if check_move(board, sq, n) == True:
		board[int(sq[0])][int(sq[1])] = marker
	else:
		print "Invalid move"

"""
    Function: play_next_move
    Purpose: trys to play move with current input
    Calls: move
"""

def play_next_move(board, sq, turn, n):
	try:
		move(board, sq, turn, n)

	except ValueError:
		print "Enter a valid move corresponding to the row & col"
"""
    Function: whos_first
    Purpose: returns string randomly picked for 
             play order
    Calls: randint()
"""

def whos_first():
	if random.randint(0,1) == 0:
		return 'player1'
	else:
		return 'player2'

"""
    Function: menu()
    Purpose: Prints menu for switch
    Calls: none
"""

def menu(n):

	print '\n\tEnter the two digit number ( 00 -', str(n-1)+str(n-1),' ) that represents the row & column of the square you wish to play on', 
	print """
	\n\t's' -- save the game
	\n\t'h' -- display help
	\n\t'p' -- print the board
	\n\t'r' -- resign
	\n\t'x' -- quit without saving
	\n\t'q' -- save quit
	"""

"""
    Function: reset
    Purpose: returns a blank board
    Calls:
"""

def reset(board, n):
	board = [['#' for col in range(n)] for row in range(n)]
	return board

"""
    Function: play
    Purpose: main function to play the game and handle file
             saves
    Calls: reset, check_move, who won, play_next_move
"""

def play():
	print "Welcome to Tic Tac Toe!"
	load = raw_input("Do you wish to load a previous session(y/n)?")
	load = load.lower()
	if load == 'y':
        #read in formatted output to variables that track the game
		file = raw_input("Enter file name: ")
		with open(file, 'r') as ins:
			lines = ins.readlines()
			player1_name = lines[0]
			x_wins = int(lines[1])
			player2_name = lines[2]
			o_wins = int(lines[3])
			draws = int(lines[4])
			n = int(lines[5])
			board = json.loads(lines[6]) #load the board 
			turn = lines[7]
			p1 = (player1_name, 'x') #tuples to assign players
			p2 = (player2_name, 'o') #x player is always top of output file
	else:
		o_wins = 0
		x_wins = 0
		draws = 0
		player1_name = raw_input("Enter player 1's name: ")
		player2_name = raw_input("Enter player 2's name: ")
		try:
			n = int(raw_input('Enter the square board size (e.g 4 for 4x4) from 3-10: '))
		except SyntaxError and NameError and ValueError as e:
			n = 4
		while n < 3 or n > 100:
			try:
				n = int(raw_input('Enter the square board size (e.g 4 for 4x4) from 3-10: '))
			except SyntaxError and NameError and ValueError as e:
				n = 4
		board = [['#' for col in range(n)] for row in range(n)]
		if (whos_first() == 'player1'): #randomly see who goes first
			print player1_name + ' is x\'s and will go first'
			p1 = (player1_name, 'x')
			p2 = (player2_name, 'o')
		else:
			print player2_name + ' is x\'s and will go first'
			p1 = (player1_name, 'o')
			p2 = (player2_name, 'x')
			
	print_board(board, n)
	turn  = 1 #turn counter
	menu(n)
	case = ''
	while case != 'q': #switch like while loop
		if turn %2 == 0: #o's turns are even
			print 'o\'s turn'
		else:
			print 'x\'s turn'
		case = raw_input("Enter your move or 'h' for help: ")
		case = case.lower()
		if case.isdigit(): #if a digit is entered make a move
			#case = int(case)
			if turn % 2 == 0: #check move, play move, check for win
				if(check_move(board, case, n)):
					play_next_move(board, case, 'o', n)
				else:
					print 'Invalid move'
					continue
				turn += 1
				if who_won(board) == 'o':
					print 'o won!'
					o_wins += 1
					turn = 1
					print 'x won ' + str(x_wins).strip('\n') + ', o won ' + str(o_wins).strip('\n') + ', there are ' + str(draws).strip('\n') + ' draws'
					choice = raw_input('do you want to play again(y)? ')
					if choice == 'n' or choice == 'N':
						break					
					board = reset(board, n)
			else:
				if(check_move(board, case, n)):
					play_next_move(board, case, 'x', n)
				else:
					print 'Invalid move'
					continue
				turn += 1
				if who_won(board) == 'x':
					print 'x won!'
					x_wins += 1
					turn = 1
					print 'x won ' + str(x_wins).strip('\n') + ', o won ' + str(o_wins).strip('\n') + ', there are ' + str(draws).strip('\n') + ' draws'
					choice = raw_input('do you want to play again(y)? ')
					if choice == 'n' or choice == 'N':
						break					
					board = reset(board, n)
			if turn > ( (n*(n+1))/2 )+1:
				print 'This game is a tie'
				draws += 1
				turn  = 1
				print 'x won ' + str(x_wins).strip('\n') + ', o won ' + str(o_wins).strip('\n') + ', there are ' + str(draws).strip('\n') + ' draws'
				choice = raw_input('do you want to play again(y)? ')
				if choice == 'n' or choice == 'N':
					break				
				board = reset(board, n)
		elif case == 'p': #print
			print_board(board, n)
		elif case == 'q' or case == 'x': #quit
				break
		elif case == 'h': #help
			print_help(n)
		elif case == 'r': #resign
			if turn %2 == 0:
				print 'x won!'
				x_wins +=1
				turn = 1
				board = reset(board, n)
			else:
				print 'o won!'
				o_wins += 1
				turn = 1
				board = reset(board, n)
			print 'x won ' + str(x_wins).strip('\n') + ', o won ' + str(o_wins).strip('\n') + ', there are ' + str(draws).strip('\n') + ' draws'
			choice = raw_input('do you want to play again(y)? ')
			if choice == 'N' or choice == 'n':
				break
		elif case == 's':
            #strip the strings of the newline character then output into file
			file = raw_input('Enter filename to save as: ')
			p1Out = player1_name.strip('\n')
			p2Out = player2_name.strip('\n')
			xOut = str(x_wins).strip('\n')
			oOut = str(o_wins).strip('\n')
			drawOut = str(draws).strip('\n')
			turnOut = str(turn).strip('\n')
			try:
				with open(file, 'r+') as outs:
					if p1[1] == 'x':
						outs.write(p1Out)
						outs.write('\n')
						outs.write(xOut)
						outs.write('\n')
						outs.write(p2Out)
						outs.write('\n')
						outs.write(oOut)
					else:
						outs.write(p2Out)
						outs.write('\n')
						outs.write(xOut)
						outs.write('\n')
						outs.write(p1Out)
						outs.write('\n')
						outs.write(oOut)
					outs.write('\n')
					outs.write(drawOut)
					outs.write('\n')
					outs.write(str(n))
					outs.write('\n')
					json.dump(board, outs) #dump the board
					outs.write('\n')
					outs.write(turnOut)
			except IOError as e:
				print 'Invalid File name or file does not exist'
		else:
			print('Invalid choice')
			continue

play()





