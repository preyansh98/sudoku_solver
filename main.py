#!/usr/bin/python3

def __main__():
    print("Welcome to Sudoku 9x9 Solver!!")
    print("Please enter all four rows of your sudoku board in the following format:")
    print("1,-1,-1,4,5,6,7,-1,9")
    print("i.e. separated by commas with no spaces, and -1 indicates an empty column, then press enter")
    print("---------------------------------------------------------------")

    print("Please enter your board:")
    
    board = getInputBoard()
    print("Board Before::")
    print(board)
    print("Board After::")
    solve(board)
    print(board)

def getInputBoard():
    _rowno = 0
    board = []

    while(_rowno is not size):
        row = str(input())
        row = [int(i) for i in row.split(",")]
        
        if len(row) is not size:
            print("Invalid Input! Terminating!")
            quit()

        board.append(row)
        _rowno += 1

    return board

#backtrack by all candidates. 
def solve(board):    
    i,j = findNext(board)

    if i == -1:
        return True

    for cand in range(1,size+1):
        if valid(board,i,j,cand):
            board[i][j] = cand

            if solve(board):
                return True

            board[i][j] = -1

    return False

def valid(board,i, j, cand):
    
    #col
    for x in range(size):
        if board[x][j] == cand and x != i:
            return False

    #row
    for x in range(size):
        if board[i][x] == cand and j != x:
            return False

    topForJ = (j // 3) * 3
    topForI = (i // 3) * 3

    for x in range(topForI, topForI + 3):
        for y in range(topForJ, topForJ + 3):
            if board[x][y] == cand and (x,y) != (i,j):
                return False

    return True

def findNext(board):
    for row in range(size):
        for col in range(size):
            if(board[row][col] == -1):
                return row,col
                 
    return -1,-1
 
#sample board
def init_sample_board():
    sample_board = [[-1, -1, -1, 2, 6, -1, 7, -1, 1], 
                    [6, 8,-1,-1,7,-1,-1,9,-1], 
                    [1,9,-1,-1,-1,4,5,-1,-1],
                    [8,2,-1,1,-1,-1,-1,4,-1],
                    [-1,-1,4,6,-1,2,9,-1,-1],
                    [-1,5,-1,-1,-1,3,-1,2,8],
                    [-1,-1,9,3,-1,-1,-1,7,4],
                    [-1,4,-1,-1,5,-1,-1,3,6],
                    [7,-1,3,-1,1,8,-1,-1,-1]]
    return sample_board

size = 9

if __name__ == "__main__":
    __main__()
