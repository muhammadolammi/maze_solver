from graphics import Window
from cell import Cell
from tkinter import Button
import time
import random
class Maze:
    def __init__(self, x1,y1,num_cols,num_rows, cell_width, cell_height, win:Window=None, seed=None ):
        self._win = win
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._num_cols = num_cols
        self._num_rows = num_rows
        self._x1 = x1
        self._y1 = y1
        self._cells = []
        self._button_solve = Button(self._win.get_root(), text="Solve", command=self.solve)
        self._button_solve.pack()
        # self.__button_reset = Button(self._win.get_root(), text="Reset", command=self.reset)
        # self.__button_reset.pack()
        
        
        if seed !=None:
            random.seed(seed)
        
        self._create_cells()
        
        self._break_entrance_and_exit()
        self._break_walls_r()
        # self._win.redraw()
        self._reset_cells_visited()
    
    #create cell for the input collumn and row
    def _create_cells(self):
        for _ in range(self._num_cols):
            cols =[]
            for _ in range(self._num_rows):
                cols.append(Cell(self._win))
            self._cells.append(cols)
        for i in range(self._num_cols):
            
            for j in range(self._num_rows):
                self._draw_cell(i,j)
    #draw each cell in the 2d list
    def _draw_cell(self, i, j):
        x1 = self._x1 + i * self._cell_width
        y1 = self._y1 + j * self._cell_height
        x2 = x1 + self._cell_width
        y2 = y1 + self._cell_width
        self._cells[i][j].draw(x1,y1,x2,y2)
        
        
    def _animate(self, speed):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(speed)
    
    #break entrance and exit
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[len(self._cells)-1][len(self._cells[0])-1].has_bottom_wall = False
        self._draw_cell(len(self._cells)-1,len(self._cells[0])-1)
    
    #break random walls 
    def _break_walls_r(self, i=1,j=1):
        
        self._cells[i][j].visited = True
        while True:
            index_to_visit =[]
            #left
            if i > 0 and not self._cells[i-1][j].visited:
                index_to_visit.append((i-1,j))
            #right
            if i < self._num_cols-1 and not self._cells[i+1][j].visited:
                index_to_visit.append((i+1,j))
            # up
            if j >0 and not self._cells[i][j-1].visited :
                index_to_visit.append((i, j-1))
            #down
            if j <self._num_rows-1 and self._cells[i][j+1].visited == False :
                index_to_visit.append((i,j+1))

            if  len(index_to_visit) ==0:
                self._draw_cell(i,j)
                return 
            
            
            
            # randomly choose the next direction to go
            direction_index = random.randrange(len(index_to_visit))
            next_index = index_to_visit[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self._break_walls_r(next_index[0], next_index[1])
        
        
        
            
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        print("maze solved")
        return self._solve_r(0,0)
        
    
    def _solve_r(self, i,j):
        self._animate(0.0005)

        # vist the current cell
        self._cells[i][j].visited = True

        # if we are at the end cell, we are done!
        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

        # move left if there is no wall and it hasn't been visited
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)

        # move right if there is no wall and it hasn't been visited
        if (
            i < self._num_cols - 1
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        # move up if there is no wall and it hasn't been visited
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        # move down if there is no wall and it hasn't been visited
        if (
            j < self._num_rows - 1
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        # we went the wrong way let the previous cell know by returning False
        return False
    
    def reset_walls(self):
        for col in self._cells:
            for cell in col:
                cell.has_top_wall =True
                cell.has_bottom_wall =True
                cell.has_right_wall=True
                cell.has_left_wall =True
    
    # def reset(self):
    #     self._win.redraw()
        
    #     self._reset_cells_visited()
    #     self.reset_walls()
        
        
    #     self._break_walls_r()
        
    #     print("Maze reset")

    





    
        






