#Logical implementation of Othello.

class Board:

    def __init__(self):
        self._turn = 0
        self._rows = 0
        self._cols = 0
        self._win_rules = ''


    def create_board(self, rows, cols) -> None:
        '''Creates a board with the given rows and columns'''
        
        try:
            if check_valid_board(rows, cols):
                self._board = []
                for row in range(rows):
                    self._board.append([])
                    for col in range(cols):
                        self._board[row].append('.')
                self._cols = len(self._board[0])
                self._rows = len(self._board)
        except:
            pass

 
    def set_board(self, color) -> None:
        '''Sets the middle four pieces of the board based on the top-left color given'''
        
        self._board[int(self._rows/2) - 1][int(self._cols/2) -1] = color
        self._board[int(self._rows/2)][int(self._cols/2)] = color

        if color == 'W':
            self._board[int(self._rows/2)-1][int(self._cols/2)] = 'B'
            self._board[int(self._rows/2)][int(self._cols/2) -1] = 'B'
        elif color == 'B':
            self._board[int(self._rows/2)-1][int(self._cols/2)] = 'W'
            self._board[int(self._rows/2)][int(self._cols/2) -1] = 'W'
            
            
    def print_board(self) -> None:
        '''Prints the current state of the board'''
        
        for row in range(len(self._board)):
            for col in range(len(self._board[row])):
                print(self._board[row][col], end = ' ')
            print('')


    def cell_state(self, row, col) -> int:
        '''Returns the state of the given cell'''
        
        if row < 0 or col < 0:
            pass
        cell = self._board[row][col]
        if cell == 'B':
            return -1
        if cell == 'W':
            return 1
        if cell == '.':
            return 0


    def blk_moves_left(self):
        '''Returns the number of possible moves black has'''
        
        turn = self._turn
        moves_left = 0
        self._turn = -1
        for row in range(self._rows):
            for col in range(self._cols):
                if self.cell_state(row, col) == 0:
                    moves_left += len(self.flipped_pieces(row,col))

        self._turn = turn
        return moves_left != 0
                    

    def wht_moves_left(self):
        '''Returns the number of possible moves white has'''
        
        turn = self._turn
        moves_left = 0
        self._turn = 1
        for row in range(self._rows):
            for col in range(self._cols):
                if self.cell_state(row, col) == 0:
                    moves_left += len(self.flipped_pieces(row,col))

        self._turn = turn
        return moves_left != 0
    

    def rows(self):
        '''Returns how many rows are on the board'''
        
        return self._rows
    

    def cols(self):
        '''Returns how many columns are on the board'''
        
        return self._cols
    

    def turn(self):
        '''Returns whose turn it is'''
        
        return self._turn
        

    def make_move(self, row, col) -> None:
        '''Executes the move given, if possible, and flips the corresponding cells'''
        
        try:

            if self.game_is_over():
                self._turn = 0

                          
            if self._board[row][col] == '.' and self.is_valid_move(row, col):   
                if self._turn == -1:
                    for cell in self.flipped_pieces(row, col):
                        self._board[cell[0]][cell[1]] = 'B'
                        self._board[row][col] = 'B'
                elif self._turn == 1:
                    for cell in self.flipped_pieces(row, col):
                        self._board[cell[0]][cell[1]] = 'W'
                        self._board[row][col] = 'W'
                self._turn *= -1

            if ((self._turn == 1 and not self.wht_moves_left())
                or
                (self._turn == -1 and not self.blk_moves_left())):
                self._turn *= -1
        except:
            pass


    def flipped_pieces(self, row, col) -> [[int]]:
        '''Given a cell, returns a list of positions that would be flipped if a move was made'''
        
        directions = [ [1,0], [-1,0], [0,1], [0,-1], [1,-1], [-1,1], [1,1], [-1,-1] ]
        total_captured = []
        for direction in directions:
            captured = []
            r, c = direction[0] + row, direction[1] + col
            while self.is_valid_cell(r,c):
                if self.cell_state(r, c) == -1 * self._turn:
                    captured.append((r,c))
                    r, c = r+direction[0], c+direction[1]
                elif self.cell_state(r,c) == self._turn:
                    total_captured += captured
                    break
                else:
                    break
        return total_captured


    def get_score(self) -> (int, int):
        '''Returns the amount of tiles each player currently has on the board'''
        
        blk_score = 0
        wht_score = 0
        for row in range(self._rows):
            for col in range(self._cols):
                if self.cell_state(row, col) == -1:
                    blk_score += 1
                if self.cell_state(row,col) == 1:
                    wht_score += 1
        return (blk_score, wht_score)


    def find_winner(self) -> str:
        '''Determines the winning player based on the rules given'''
        
        blk, wht = self.get_score()
        
        if blk > wht:
            bigger = 'Black'
            smaller = 'White'
        elif wht > blk:
            bigger = 'White'
            smaller = 'Black'
        else:
            bigger = 'NONE'
            smaller = 'NONE'
            
        if self._win_rules == '>':
            return bigger            
        elif self._win_rules == '<':
            return smaller


    def is_valid_move(self, row, col) -> bool:
        '''Determines if a move is valid'''
        
        if len(self.flipped_pieces(row, col)) == 0:
            return False
        return True

    
    def is_valid_cell(self, row, col) -> bool:
        '''Determines if a cell is on the board'''
        
        return row >= 0 and row < self._rows and col >= 0 and col < self._cols


    def game_is_over(self) -> bool:
        '''Determines if there are any possible moves left'''
        
        return (not self.blk_moves_left()) and (not self.wht_moves_left())




def convert_int(turn: int) -> str:
    '''Converts between arbitrary int values to the corresponding str values'''
    if turn == -1:
        return('B')
    elif turn == 1:
        return('W')
    elif turn == 0:
        return('NONE')
    

def convert_str(turn: str) -> int:
    '''Converts between the arbitrary str values to the corresponding int values'''   
    if turn == 'B':
        return -1
    elif turn == 'W':
        return 1
    elif turn == 'NONE':
        return 0

def check_valid_board(row, col) -> bool:
    '''Checks if the given board dimensions are legal'''
    
    try:
        return row%2 == 0 and row >= 4 and row <= 16 and col%2 == 0 and col >= 4 and col <= 16
    except:
        pass
