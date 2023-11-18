from graphics import Window 
import sys
sys.setrecursionlimit(10000)  # Set an appropriate limit


from maze import Maze

def main():
    win =Window(600,600)
    x1=5
    y1=5
    num_cols = 118
    num_rows=118
    cell_width = 5
    cell_height = 5
    m1 = Maze(x1,y1, num_cols, num_rows, cell_width,cell_height, win)
    
    
    win.wait_for_close()

main()