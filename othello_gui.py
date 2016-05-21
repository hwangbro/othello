#Code behind the graphical interface of Othello


import point
import tkinter as tk
import tile
import othello_logic
import game_options


_DEFAULT_FONT = ('Verdana', 16)

class BoardGUI:

    def __init__(self, window, board):
        self._tiles = []
        self._window = window
        self._board = board
        
        self._rows = self._board.rows()
        self._cols = self._board.cols()
        
        self._canvas = tk.Canvas(master = self._window,
                                 height = 450, width = 450,
                                 background = '#80E6FF')
        self._canvas.grid(row = 1, column = 0,
                          sticky = tk.N + tk.W + tk.S + tk.E)
        
        self._window.rowconfigure(1, weight = 1)
        self._window.columnconfigure(0, weight = 1)


    def _draw_tiles(self) -> None:
        '''Draws the tiles onto the board'''
        
        self._tiles = []
        self.width = self._canvas.winfo_width()
        self.height = self._canvas.winfo_height()
        
        for i in range(self._rows):
            self._tiles.append([])
            for j in range(self._cols):
                cell = tile.Tile(i, j)
                self._tiles[i].append(cell)
                cell.draw(self._canvas,
                          tile.create_tile_points(i, j, self._rows,self._cols))


    def _draw_pieces(self) -> None:
        '''Draws the black and white pieces onto the board'''
        
        for row in range(self._board.rows()):
            for col in range(self._board.cols()):
                color = self._board.cell_state(row, col)
                tile = self._tiles[row][col]
                if color == -1:
                    self._canvas.create_oval(
                        tile.tl.pixel(self.width, self.height)[0],
                        tile.tl.pixel(self.width, self.height)[1],
                        tile.br.pixel(self.width, self.height)[0],
                        tile.br.pixel(self.width, self.height)[1],
                        fill = '#000000')
                    
                if color == 1:
                    self._canvas.create_oval(
                        tile.tl.pixel(self.width, self.height)[0],
                        tile.tl.pixel(self.width, self.height)[1],
                        tile.br.pixel(self.width, self.height)[0],
                        tile.br.pixel(self.width, self.height)[1],
                        fill = '#FFFFFF')


    def _draw_board(self) -> None:
        '''Draws the board'''
        
        self._canvas.delete(tk.ALL)
        self._draw_tiles()
        self._draw_pieces()


class OthelloApplication:
    def __init__(self, board):
        self._board = board
        self._root_window = tk.Tk()
        self._root_window.minsize(400,400)
        
        self._turn = tk.StringVar()
        self._turn.set('')

        self._blk_score = tk.StringVar()
        self._blk_score.set('Black: 0')
        
        self._wht_score = tk.StringVar()
        self._blk_score.set('White: 0')

        label_frame = tk.Frame(
            master = self._root_window)
        label_frame.grid(row = 0, column = 0, padx = 10, pady = 10,
                         sticky = tk.N + tk.S + tk.E + tk.W)

        turn_label = tk.Label(
            master = label_frame,
            textvariable = self._turn,
            font = _DEFAULT_FONT)
        turn_label.grid(row = 0, column = 1, padx = 10, sticky = tk.N)

        blk_score_label = tk.Label(
            master = label_frame,
            textvariable = self._blk_score,
            font = _DEFAULT_FONT)
        blk_score_label.grid(row = 0, column = 0, padx = 10, sticky = tk.W + tk.N)

        wht_score_label = tk.Label(
            master = label_frame,
            textvariable = self._wht_score,
            font = _DEFAULT_FONT)
        wht_score_label.grid(row = 0, column = 2, padx = 10, sticky = tk.E + tk.N)

        label_frame.columnconfigure(0, weight = 1)
        label_frame.columnconfigure(1, weight = 1)
        label_frame.columnconfigure(2, weight = 1)

        self.update_score()
        self.update_turn()

        self._boardGUI = BoardGUI(self._root_window, self._board)
        self._boardGUI._canvas.bind('<Configure>', self._on_canvas_resized)
        self._boardGUI._canvas.bind('<Button-1>', self._on_tile_clicked)
        

    def _on_canvas_resized(self, event: tk.Event) -> None:
        '''Re-draws the board when the window is resized'''
        
        self._boardGUI._draw_board()
        

    def _on_tile_clicked(self, event: tk.Event) -> None:
        '''Makes a move, if possible, on the tile clicked'''
        
        click_point = point.from_pixel(event.x, event.y, self._boardGUI.width, self._boardGUI.height)

        for row in range(len(self._boardGUI._tiles)):
            for col in range(len(self._boardGUI._tiles[row])):
                if self._boardGUI._tiles[row][col].contains(click_point):
                    self._board.make_move(row, col)
                    self._boardGUI._draw_board()

        self.update_score()
        self.update_turn()
        

    def start(self) -> None:
        '''Starts the application'''
        
        self._root_window.mainloop()
        

    def update_score(self) -> None:
        '''Updates the score labels on the window'''
        
        self._blk_score.set('Black:{}'.format(self._board.get_score()[0]))
        self._wht_score.set('White:{}'.format(self._board.get_score()[1]))
        

    def update_turn(self) -> None:
        '''Updates the turn label on the window'''
        
        turn = convert_color(self._board.turn())
        if self._board.game_is_over():
            self._turn.set('Winner:{}'.format(self._board.find_winner()))
        else:
            self._turn.set('Turn:{}'.format(turn))



def create_board() -> othello_logic.Board:
    '''Creates the option menu and uses the inputs to create an othello board'''
    
    menu = game_options.OptionMenu()
    inputs = menu.answers
    if len(inputs) != 0:   
        game = othello_logic.Board()
        game.create_board(inputs[0], inputs[1])
        game._turn = othello_logic.convert_str(inputs[2])
        game.set_board(inputs[3])
        game._win_rules = inputs[4]
        return game
    else:
        raise InputError
    

def convert_color(color: int) -> str:
    '''Translates the int representation of color into str'''
    
    if color == 1:
        return 'White'
    if color == -1:
        return 'Black'
    if color == 0:
        return 'None'
    

def run_othello() -> None:
    '''Creates and runs an instance of Othello'''
    
    try:
        game_board = create_board()
        app = OthelloApplication(game_board)
        app.start()
    except:
        pass

if __name__ == '__main__':
    run_othello()
