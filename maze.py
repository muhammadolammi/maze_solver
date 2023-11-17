from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed = None
    ):
        self._x1 = x1
        self._y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._seed = seed

        self._create_cells()
        if self._seed is not None:
            random.seed(seed)
    
    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self._win))
            self._cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        
        if self._win is None:
            return 
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1,y1,x2,y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return 
        self._win.redraw()
        time.sleep(0.02)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)
    
    def get_unvisited_neighbors(self, i,j):
        neigbors = []
        if i > 0 and self._cells[i-1][j].visited == False:
            neigbors.append((i-1,j))
        if i < len(self._cells)-1 and self._cells[i+1][j].visited == False:
            neigbors.append((i+1,j))
        
        if j > 0  and self._cells[i][j-1].visited ==False:
            neigbors.append((i,j-1))
        if j < len(self._cells[i])-1  and self._cells[i][j+1].visited ==False:
            neigbors.append((i,j+1))
        
        return neigbors





    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        
        while True:
            # Check the cells that are directly adjacent to the current cell
            neighbors = self.get_unvisited_neighbors(i, j)

            # If there are zero directions, draw the current cell and return
            if not neighbors:
                # Draw the current cell 
                self._draw_cell(i, j)  # Assuming draw takes (i, j) as arguments
                return

            # Otherwise, pick a random direction
            next_i, next_j = random.choice(neighbors)

            # Knock down the walls between the current cell and the chosen cell
            if i > next_i:
                self._cells[i][j].has_top_wall = False
                self._cells[next_i][next_j].has_bottom_wall = False
            if i < next_i:
                self._cells[i][j].has_bottom_wall = False
                self._cells[next_i][next_j].has_top_wall = False
            if j > next_j:
                self._cells[i][j].has_left_wall = False
                self._cells[next_i][next_j].has_right_wall = False
            if j < next_j:
                self._cells[i][j].has_right_wall = False
                self._cells[next_i][next_j].has_left_wall = False

            # Move to the chosen cell by recursively calling _break_walls_r
            if not self._cells[next_i][next_j].visited:
                self._break_walls_r(next_i, next_j)
        

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
