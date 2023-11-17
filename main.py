from graphics import Window ,Point,Line
from cell import Cell
from maze import Maze

def main():
    win =Window(800,620)
    x1=10
    y1=10
    num_cols = 15
    num_rows=12
    cell_width = 50
    cell_height = 50
    m1 = Maze(x1,y1, num_cols, num_rows, cell_width,cell_height, win)
    
    
    win.wait_for_close()

main()