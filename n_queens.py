n = 4
Board = []
blocked = []
placed = []
row_increase,wait = True,True
row = 0
removed = []

import sys
sys.setrecursionlimit(10**6)

def board() :
    for i in range(1,n+1) :
        coordinates = []
        for j in range(1,n+1) :
            coordinates.append('-')
        Board.append(coordinates)
    return Board

def placing_queens(Board) :
    global row,row_increase,wait
    row_increase,wait = True,True

    if row > n-1 :
        print(row)
        print("SOLVED")
        wait = False
        return

    for j in range(n) :
        if Board[row][j] == '-' :
            Board[row][j] = 1
            placed.append((row,j))
            blocking(row,j,Board)
            return

    else :
        backtrack()

#--------------------------------- Backtracking  ---------------------------#

def backtrack() :
    
    global placed ,Board,row,row_increase,removed,wait
    Board = []
    new_board = board()
    poped = placed.pop()
    removed.append(poped)

    # Removing unsuitable places
    for i in removed :
        if row > i[0] : 
            new_board[i[0]][i[1]] = 1
        else :
            removed.remove(i)

    # reducing row size while backtracking
    row -= 1
    row_increase = False
    
    # When come to the first place then remove all blocking posibilities  
    if len(placed) == 0 :
        print(removed,'-')
        removed = []
        new_board[poped[0]][poped[1]] = 1
        placing_queens(new_board)
        return

    # After removing unsuitable places blocking other placing of other queen
    for i in placed :
        wait = False
        blocking(i[0],i[1],new_board)

    placing_queens(new_board)

#--------------------------------- BLOCKING BOXES ---------------------------#

def blocking(x,y,Board) : 
    global row,wait
    # row and column
    for i in range(n) :
        Board[x][i] = 'B'
        Board[i][y] = 'B'
    
    # diagonal blocking
    for i in range(n) :
        for j in range(n) :
            if i+j == x+y :
                Board[i][j] = 'B' 
            if i-j == x-y :
                Board[i][j] = 'B'

    if row_increase == True :
        row += 1
    if wait == True :
        placing_queens(Board)

#--------------------------------- Main ---------------------------#

board()
placing_queens(Board)

#---------------------------------- Printing solution ------------------------------------------#

for i in placed:
    Board[i[0]][i[1]] = 'placed'

print(f'Placed positions { placed }')

for i in Board:
    print(i)