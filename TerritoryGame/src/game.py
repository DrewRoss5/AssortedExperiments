import sys

class GameBoard:
    SYMBOLS = [' ', '█']
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.board = [0] * (width * height)

    def get_cell(self, x: int, y: int):
        if (x > self.width or y > self.height or x < 0 or y < 0):
            raise ValueError('Invalid access coords')
        return self.board[(self.width * y) + x]

    def fill_cell(self, x: int, y: int):
        if (x > self.width or y > self.height or x < 0 or y < 0):
            raise ValueError('Invalid access coords')
        self.board[(self.width * y) + x] = 1

    def display(self, stdscr):
        stdscr.move(1, 1)
        out = ''
        col = 0
        row = 0
        for cell in self.board:
            out += self.SYMBOLS[cell]
            col += 1
            if (col == self.width):
                stdscr.addstr(out)
                row += 1
                col = 0
                stdscr.move(row, 1)
                out = ''
        stdscr.refresh()
