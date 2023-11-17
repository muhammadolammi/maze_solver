from tkinter import Tk, BOTH, Canvas,Button
class Point:
    def __init__(self, x, y) :
        self.x =x
        self.y =y
class Line:
    def __init__(self, point1:Point, point2:Point):
        self.x1=point1.x
        self.x2=point2.x
        self.y1 =point1.y
        self.y2 = point2.y
    def draw_line(self, canvas:Canvas, fill_color):
        canvas.create_line(self.x1, self.y1, self.x2,self.y2,fill=fill_color)
        canvas.pack(fill=BOTH, expand=1)
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False

        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        
        
    def get_root(self):
        return self.__root
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    def close(self):
        self.__running = False
    
    def draw_line(self, line:Line, fill_color):
        line.draw_line(self.__canvas, fill_color)
    
    def button_click(self):
        print("Clicked")

    