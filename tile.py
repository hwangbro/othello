#Logical class behind a "tile" concept in Othello.

import point

class Tile:
    
    def __init__(self, row: int, col: int):
        self.tl, self.br = None, None
        self._row = 0
        self._col = 0

    def contains(self, p: point.Point) -> bool:
        '''Determines if a point is in a given tile'''
        
        px, py = p.frac()
        return (px <= self.br_x and px >= self.tl_x) and (py <= self.br_y and py >= self.tl_y)


    def row(self) -> int:
        '''Returns the row of the tile'''
        
        return self._row

    def col(self) -> int:
        '''Returns the column of the tile'''
        
        return self._col

    def draw(self, canvas, points) -> None:
        '''Draws the tile onto a given canvas'''
        
        self.tl, self.br = points
        self.tl_x, self.tl_y = self.tl.frac()
        self.br_x, self.br_y = self.br.frac()
        width = canvas.winfo_width()
        height = canvas.winfo_height()
        point_pixels = []
        for point in points:
            point_pixels.append(point.pixel(width, height))

        canvas.create_rectangle(point_pixels[0][0],
                                point_pixels[0][1],
                                point_pixels[1][0],
                                point_pixels[1][1],
                                fill = '#FFBF5E')
        

def create_tile_points(row, col, total_row, total_col) -> (point.Point):
    '''Returns the top-left and bottom-right points of a box with the given row and column'''
    
    x = (.9 / total_col)
    y = (.9 / total_row)
    pad = 0.05

    return(point.from_frac( (pad + (x*col)), (pad + (y*row))),
           point.from_frac( (pad + (x*(col+1))), (pad + (y*(row+1)))))
