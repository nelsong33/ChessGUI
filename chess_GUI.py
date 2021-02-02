from tkinter import *


class chessBoard:

    def __init__(self, master, window_title, initial_position):
        self.master = master
        master.title(window_title)
        master.resizable(False, False)

        canvas = Canvas(master, bg="white", width=800, height=480, highlightthickness=0)
        canvas.create_rectangle(480, 0, 485, 480, outline="black", fill="black")
        canvas.pack()

        self.board = Frame(master, bg="black")
        self.board.place(relx=0, rely=0, relwidth=.6, relheight=1)

        self.board_grid = []  # each square on board with info [alpha-numerical position, label object]
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        self.dark = "#0c2663"
        self.light = "#e6e4df"
        for i in range(4):
            new1 = []
            for j in range(1, 5):
                new1.append((letters[2 * i] + str(2 * j - 1), Label(self.board, bg=self.dark)))
                new1.append((letters[2 * i] + str(2 * j), Label(self.board, bg=self.light)))
                new1[2 * (j - 1)][1].place(relx=((2 * i) * .125), rely=(1 - ((2 * j - 1) * .125)), relwidth=.125,
                                           relheight=.125)
                new1[2 * j - 1][1].place(relx=((2 * i) * .125), rely=(1 - ((2 * j) * .125)), relwidth=.125,
                                         relheight=.125)
            new2 = []
            for j in range(1, 5):
                new2.append((letters[2 * i + 1] + str(2 * j - 1), Label(self.board, bg=self.light)))
                new2.append((letters[2 * i + 1] + str(2 * j), Label(self.board, bg=self.dark)))
                new2[2 * (j - 1)][1].place(relx=((2 * i + 1) * .125), rely=(1 - ((2 * j - 1) * .125)),
                                           relwidth=.125,
                                           relheight=.125)
                new2[2 * j - 1][1].place(relx=((2 * i + 1) * .125), rely=(1 - ((2 * j) * .125)), relwidth=.125,
                                         relheight=.125)
            self.board_grid.append(new1)
            self.board_grid.append(new2)
        self.board_setup(initial_position)
    pass

    def board_setup(self, initial_position):
        for i in initial_position:
            self.board_grid[i.x][i.y][1].config(image=i.img)
    pass

    def move(self, init_pos, fin_pos):
        p = self.board_grid[init_pos[0]][init_pos[1]][1].cget('image')
        self.board_grid[fin_pos[0]][fin_pos[1]][1].config(image=p)
        self.board_grid[init_pos[0]][init_pos[1]][1].config(image='')
    pass


pass






