def printBoard(board):
    print("\n\nCurrnt board:\n")
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print(f'--|---|---')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'--|---|---')
    print(f'{board[6]} | {board[7]} | {board[8]}')
 

def boardEditor(xState, oState):
    global flag
    boardStatus = [0,1,2,3,4,5,6,7,8]
    for i in range(9):
        boardStatus[i] = 'X' if xState[i] else ('O' if oState[i] else boardStatus[i])
    
    printBoard(boardStatus)
    gameStatus(boardStatus)

    if all(isinstance(item,str) for item in boardStatus):
        flag = False
        print("\nMatch Drawn!!!")


def gameStatus(boardStatus):
    global flag
    winPatterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in winPatterns:
        if(boardStatus[win[0]] == boardStatus[win[1]] == boardStatus[win[2]] == 'X'):
           flag = False
           print("\n\n\n\t\tPlayer 1 wins!!!")
        elif(boardStatus[win[0]] == boardStatus[win[1]] == boardStatus[win[2]] == 'O'):
           flag = False
           print("\n\n\n\t\tPlayer 2 wins!!!")


if __name__ == '__main__':
    xState = [0,0,0,0,0,0,0,0,0]
    oState = [0,0,0,0,0,0,0,0,0]
    print("\t\tWelcome to Tic Tac Toe:\n")
    turn = 1
    global flag
    flag = True

    while(True):
        
        boardEditor(xState,oState)
        if not flag : break
        
        try:
            if turn==1:
                print("\nPlayer 1's turn: ")
                print("Enter the box in which you want to place X: \n")
                value = int(input())
                if oState[value]==0: xState[value]=1
                else:
                    print("\nLocation preoccupied by O!!! \nPlease enter a different location:")
                    continue

            else:
                print("\nPlayer 2's turn: ")
                print("Enter the box in which you want to place O: \n")
                value = int(input())
                if xState[value]==0: oState[value]=1
                else:
                    print("\nLocation preoccupied by X!!! \nPlease enter a different location:")
                    continue
                
        except (IndexError , ValueError):
            print("\n\nEnter a value between 0-8 only.\n\n")
            continue

        turn = 1 - turn