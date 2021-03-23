import tkinter as tk
import shape

# GLOBALS

BOARDWIDTH = 200
BOARDHEIGHT = 600

TILE_WIDTH = BOARDWIDTH // 10
TILE_HEIGHT = TILE_WIDTH

START_X, START_Y = STARTING_POS = BOARDWIDTH // 2 - TILE_WIDTH, 0

# END GLOBALS


class Display:

    def __init__(self, master=None):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=BOARDWIDTH, height=BOARDHEIGHT,
                                bg='black')

        self.shape_wallet = []
        self.insert_shape()

        self.pulse()

        self.canvas.pack()

    def insert_shape(self):
        self.shape_wallet.append(shape.Shape(owner_canvas=self.canvas, pos=STARTING_POS))
        print(STARTING_POS)

    def pulse(self):
        check = False
        for shape in self.shape_wallet:

        self.canvas.after(300, self.pulse)


def main():
    root = tk.Tk()
    base = Display(root)

    tk.mainloop()


if __name__ == '__main__':
    main()
