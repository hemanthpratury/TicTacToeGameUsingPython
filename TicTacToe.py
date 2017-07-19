from IPython.display import clear_output

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
def printBoard(board):
    h = '_'
    v = '|'
    b = ' '
    #board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    clear_output()
    print(3*b + v + 3*b + v)
    print(2*b + board[7] + v + 2*b + board[8] + v + board[9])
    print(3*h + v + 3*h + v + 3*h)
    print(3*b + v + 3*b + v)
    print(2*b + board[4] + v + 2*b + board[5] + v + board[6])
    print(3*h + v + 3*h + v +3*h)
    print(3*b + v + 3*b + v)
    print(2*b + board[1] + v + 2*b + board[2] + v + board[3])
    print(3*b + v + 3*b + v)

def winOrTie(player,marker):
    if(board[1] == board[5] == board[9] == marker
      or board[3] == board[5] == board[7] == marker
      or board[7] == board[8] == board[9] == marker
      or board[3] == board[6] == board[9] == marker
      or board[4] == board[5] == board[6] == marker
      or board[1] == board[2] == board[3] == marker
      or board[2] == board[5] == board[8] == marker
      or board[1] == board[4] == board[7] == marker):
        #return "%s is winner" %player
        status = '%s is winner' %player
        return status
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and 
         board[7]!=' ' and board[8]!=' ' and board[9]!=' '):
        status = 'Tie'
        return status
    else:
        playing = True
        return playing

def storeUserInputToList(inputPos, marker):
    global board
    board[inputPos] = marker

def mainFunction():
    playing = False
    turn = 1
    print('Please enter the User Name-')
    UserName1 = input()
    print('Please enter your choice of Marker')
    marker_User1 = input()
    print('%s uses %s marker' %(UserName1, marker_User1))
    print('Please enter the User Name-')
    UserName2 = input()
    marker_User2 = 'O'
    print('%s uses %s marker' %(UserName2, marker_User2))
    print('Positions in the game')
    printBoard([' ', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    print('====================== Game Begins =========================')
    print('')
    playing = True
    while(playing):
        if(turn%2 != 0):
            print("%s's turn" %(UserName1))
        else:
            print("%s's turn" %(UserName1))
        print("Enter position you want to place your marker")
        marker_pos = int(input())
        if(turn%2 != 0):
            storeUserInputToList(marker_pos, marker_User1)
            winner_str = winOrTie(UserName1,marker_User1)
            local_str = '%s is winner' %UserName1
            if(winner_str == local_str):
                print(local_str)
                break
        elif(turn%2 == 0):
            storeUserInputToList(marker_pos, marker_User2)
            winner_str = winOrTie(UserName2,marker_User2)
            local_str = '%s is winner' %UserName1
            if(winner_str == local_str):
                print(local_str)
                break
        else:
            print("There is some problem with the Turn Element")
            break
        printBoard(board)
        turn+=1


mainFunction()