import unittest
from maze import Maze
from graphics import Window

class Tests(unittest.TestCase):
    def test_maze_class(self):
        num_row = 12
        num_cols =17
        x= 20
        y = 20
        win =Window(900,650)
        m1 = Maze(x,y,num_row,num_cols, 50, 50,win , 0)
        m1._break_entrance_and_exit()
        m1._break_walls_r(0,0 )
        m1._reset_cells_visited()
        self.assertEqual(
            len(m1._cells), num_cols, 
        )
        self.assertEqual(
            len(m1._cells[0]), num_row, 
        )
    
        self.assertEqual(
            m1._cells[0][0].has_top_wall, False
        )
        self.assertEqual(
            m1._cells[num_cols-1][num_row-1].has_bottom_wall, False
        )
        for col in m1._cells:
            for cell in col:
                self.assertFalse(cell.visited)

if __name__ == "__main__":
    unittest.main()
