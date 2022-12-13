import sys
sys.setrecursionlimit(10**6)

class N_QUEENS :
    def _init_ (self) :
        self.n = 8
        self.Board = []
        self.blocked = []
        self.placed = []
        self.row_increase,wait = True,True
        self.row = 0
        self.removed = []

    def board(self) :
        for i in range(1,self.n+1) :
            coordinates = []
            for j in range(1,self.n+1) :
                coordinates.append('-')
            self.Board.append(coordinates)
        return self.Board

    def placing_queens(self,Board) :
        self.row_increase,self.wait = True,True

        if self.row > self.n-1 :
            self.solution()
            self.wait = False
            return

        for j in range(self.n) :
            if Board[self.row][j] == '-' :
                Board[self.row][j] = 1
                self.placed.append((self.row,j))
                self.blocking(self.row,j,Board)
                return

        else :
            self.backtrack()

    def backtrack(self) :
        self.Board = []
        self.new_board = self.board()
        self.poped = self.placed.pop()
        self.removed.append(self.poped)

        # Removing unsuitable places
        for i in self.removed :
            if self.row > i[0] : 
                self.new_board[i[0]][i[1]] = 1
            else :
                self.removed.remove(i)

        # reducing row size while backtracking
        self.row -= 1
        self.row_increase = False

        # When come to the first place then remove all blocking posibilities  
        if len(self.placed) == 0 :
            self.removed = []
            self.new_board[self.poped[0]][self.poped[1]] = 1
            self.placing_queens(self.new_board)
            return

        # After removing unsuitable places blocking other placing of other queen
        for i in self.placed :
            self.wait = False
            self.blocking(i[0],i[1],self.new_board)
        
        self.placing_queens(self.new_board)

#--------------------------------- Blocking Places ---------------------------#

    def blocking(self,x,y,Board) : 
        
        # row and column
        for i in range(self.n) :
            Board[x][i] = 'B'
            Board[i][y] = 'B'
        
        # diagonal blocking
        for i in range(self.n) :
            for j in range(self.n) :
                if i+j == x+y :
                    Board[i][j] = 'B' 
                if i-j == x-y :
                    Board[i][j] = 'B'

        if self.row_increase == True :
            self.row += 1
        if self.wait == True :
            self.placing_queens(Board)
        
#---------------------------------- Printing solution ------------------------------------------#

    def solution(self) :
        for i in self.placed:
            self.Board[i[0]][i[1]] = 'placed'

        print(f'Placed positions { self.placed }')

        for i in self.Board:
            print(i)

#--------------------------------- Main ---------------------------#

obj = N_QUEENS()
Creatingboard = obj.board()
obj.placing_queens(Creatingboard)