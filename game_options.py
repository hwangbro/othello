#Graphical implementation for a menu system.


import tkinter as tk

class OptionMenu:
    def __init__(self):
        self._window = tk.Tk()
        self._window.wm_title('Options Menu')
        self._window.resizable(width = False, height = False)
        
        self.answers = []

        self._create_labels()
        self._print_labels()
        self._create_option_menus()
        self._print_option_menus()
        self._create_button()
        self._print_button()

        self._window.mainloop()

        
    def _create_labels(self) -> None:
        '''Creates the labels for the option menu'''
        
        self._label_1 = tk.Label(master = self._window,
                                 text = '# of Rows',
                                 font = ('Verdana', 12))
        self._label_2 = tk.Label(master = self._window,
                                 text = '# of Cols',
                                 font = ('Verdana', 12))
        self._label_3 = tk.Label(master = self._window,
                                 text = 'Who Moves First',
                                 font = ('Verdana', 12))
        self._label_4 = tk.Label(master = self._window,
                                 text = 'Top-Left Piece',
                                 font = ('Verdana', 12))
        self._label_5 = tk.Label(master = self._window,
                                 text = 'Who Wins',
                                 font = ('Verdana', 12))


    def _print_labels(self) -> None:
        '''Prints the labels onto the window'''
        
        self._label_1.grid(row = 0, column = 0, padx = 20,
                           sticky = tk.N + tk.S + tk.E + tk.W)
        self._label_2.grid(row = 0, column = 1, padx = 20,
                           sticky = tk.N + tk.S + tk.E + tk.W)
        self._label_3.grid(row = 0, column = 2, padx = 20,
                           sticky = tk.N + tk.S + tk.E + tk.W)
        self._label_4.grid(row = 2, column = 0, padx = 20,
                           sticky = tk.N + tk.S + tk.E + tk.W)
        self._label_5.grid(row = 2, column = 1, padx = 20,
                           sticky = tk.N + tk.S + tk.E + tk.W)
        

    def _create_option_menus(self) -> None:
        '''Creates the option menu widgets'''
        
        responses_1_2 = ['4', '6', '8', '10', '12', '14', '16']
        self.response_1 = tk.StringVar()
        self.response_1.set('4')
        self._option_1 = tk.OptionMenu(self._window,
                                       self.response_1,
                                       *responses_1_2)

        self.response_2 = tk.StringVar()
        self.response_2.set('4')
        self._option_2 = tk.OptionMenu(self._window,
                                       self.response_2,
                                       *responses_1_2)

        responses_3_4 = ['Black', 'White']
        self.response_3 = tk.StringVar()
        self.response_3.set('Black')
        self._option_3 = tk.OptionMenu(self._window,
                                       self.response_3,
                                       *responses_3_4)

        self.response_4 = tk.StringVar()
        self.response_4.set('Black')
        self._option_4 = tk.OptionMenu(self._window,
                                       self.response_4,
                                       *responses_3_4)

        responses_5 = ['Most Pieces', 'Least Pieces']
        self.response_5 = tk.StringVar()
        self.response_5.set('Most Pieces')
        self._option_5 = tk.OptionMenu(self._window,
                                       self.response_5,
                                       *responses_5)
        

    def _print_option_menus(self) -> None:
        '''Prints the option menu widgets to the window'''
        
        self._option_1.grid(row = 1, column = 0, padx = 20, pady = 5,
                            sticky = tk.N + tk.S + tk.E + tk.W)
        self._option_2.grid(row = 1, column = 1, padx = 20, pady = 5,
                            sticky = tk.N + tk.S + tk.E + tk.W)
        self._option_3.grid(row = 1, column = 2, padx = 20, pady = 5,
                            sticky = tk.N + tk.S + tk.E + tk.W)
        self._option_4.grid(row = 3, column = 0, padx = 20, pady = 5,
                            sticky = tk.N + tk.S + tk.E + tk.W)
        self._option_5.grid(row = 3, column = 1, padx = 20, pady = 5,
                            sticky = tk.N + tk.S + tk.E + tk.W)
        

    def _create_button(self) -> None:
        '''Creates the start button for the option menu'''
        
        self._button = tk.Button(master = self._window, text = 'Start!',
                                 font = ('Verdana', 16),
                                 command = self._on_button_clicked)
        

    def _print_button(self) -> None:
        '''Prints the start button onto the window'''
        
        self._button.grid(row = 3, column = 2, padx = 10, pady = 10,
                          sticky = tk.N + tk.S + tk.E + tk.W)
        

    def _on_button_clicked(self) -> None:
        '''Gets the responses from the option menu and destroys the window'''
        
        self.answers = []
        self.answers.append(int(self.response_1.get()))
        self.answers.append(int(self.response_2.get()))
        self.answers.append(convert_color(self.response_3.get()))
        self.answers.append(convert_color(self.response_4.get()))
        self.answers.append(convert_winner_rule(self.response_5.get()))

        self._window.destroy()
        

def convert_color(color: str) -> str:
    '''Translates into the abbreviation for the color'''
    
    if color == 'Black':
        return 'B'
    if color == 'White':
        return 'W'
    

def convert_winner_rule(rule: str) -> str:
    '''Translates into the necessary symbol for most or least pieces'''
    
    if rule == 'Most Pieces':
        return '>'
    if rule == 'Least Pieces':
        return '<'
