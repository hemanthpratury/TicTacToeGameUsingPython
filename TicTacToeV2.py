from IPython.display import clear_output
import random

def printBoard(board):
    h = '_'
    v = '|'
    b = ' '
    clear_output()
    print(5*b + v + 5*b + v + 5*b)
    print(2*b + board[7] + 2*b + v + 2*b + board[8] + 2*b + v + 2*b + board[9] +2*b)
    print(5*h + v + 5*h + v + 5*h)
    print(5*b + v + 5*b + v + 5*b)
    print(2*b + board[4] + 2*b + v + 2*b + board[5] + 2*b + v + 2*b + board[6] +2*b)
    print(5*h + v + 5*h + v + 5*h)
    print(5*b + v + 5*b + v + 5*b)
    print(2*b + board[1] + 2*b + v + 2*b + board[2] + 2*b + v + 2*b + board[3] +2*b)
    print(5*b + v + 5*b + v + 5*b)

def playerInput(): #step 1
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = input('Player 1: Do you want to be an X or O?').upper()

    if(marker == 'X'):
        print('Player 1: X')
        print('Player 2: O')
        return ('X','O')
    else:
        print('Player 2: O')
        print('Player 1: X')
        return('O','X')


def winCheck(board,marker):
    if(board[1] == board[5] == board[9] == marker   #diagonal
      or board[3] == board[5] == board[7] == marker #diagonal
      or board[7] == board[8] == board[9] == marker #top row
      or board[3] == board[6] == board[9] == marker #last column
      or board[4] == board[5] == board[6] == marker #middle row
      or board[1] == board[2] == board[3] == marker #first row
      or board[2] == board[5] == board[8] == marker #middle col
      or board[1] == board[4] == board[7] == marker):#first col
        return True
    else:
    	return False

def chooseFirst():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def spaceCheck(board,position):
    return board[position] == ' '

def fullBoardCheck(board):
    for i in range(1,10):
        if spaceCheck(board,i):
            return False

    return True

def playerChoice(board):

    pos = ' '

    while(pos not in '1 2 3 4 5 6 7 8 9'.split() or not in spaceCheck(board,int(pos))):
        pos = input('Choose your next position: (1-9)')

    return pos

def storeUserInputToList(board,inputPos,marker):
    
    board[inputPos] = marker


def replay():

    return input('Do you want to play again? Enter Yes or No').lower().startswith('y')

def gameplay():

	print('Welcome to Tic Tac Toe!')
	print('			-Developed by Hemanth')

	while True:

		theBoard = [' ']*10
		player1_marker,player2_marker = playerInput()
		turn = chooseFirst()
		print('%s will go first' %(turn))

		game_on = True

		while(game_on):

			if turn == 'Player 1':

				printBoard(theBoard)
				position = playerChoice()
				storeUserInputToList(theBoard,position,player1_marker)
				printBoard(theBoard)

				if winCheck(theBoard,player1_marker):
					printBoard(theBoard)
					print("Congratulations! Player 1 has won")
					game_on = False

				else:
					if fullBoardCheck():
						print('It is a Tie!')
					else:
						turn = 'Player 2'


			else if turn == 'Player 2':

				printBoard(theBoard)
				position = playerChoice()
				storeUserInputToList(theBoard,position,player2_marker)
				printBoard(theBoard)

				if winCheck(theBoard,player2_marker):
					printBoard(theBoard)
					print("Congratulations! Player 2 has won")
					game_on = False

				else:
					if fullBoardCheck():
						print('It is a Tie!')
					else:
						turn = 'Player 1'

			if replay():
				continue
			else:
				break






