import unittest
from maze import Maze
from graphics import Window


class Test(unittest.TestCase):
    def test_maze(self):
        x1 = 10
        y1=10
        num_cols = 12
        num_rows = 18
        cell_height = 50
        cell_width = 50
        # win = Window(800,600)



        m1 = Maze(x1,y1,num_cols,num_rows,cell_width,cell_height, )
       

        self.assertEqual(
           len( m1._cells), num_cols
        )
        self.assertEqual(
            len(m1._cells[0]), num_rows
        )
    def test_maze_reset_cells_visted(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )

if __name__ == "__main__":
    unittest.main()