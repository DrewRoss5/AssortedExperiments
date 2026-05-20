import sys
import time
import os
import curses

import game
import algo

def print_err(err_str: str, stdscr):
    stdscr.addstr(f'Error: {err_str}\n\rPress any key to exit.')
    stdscr.refresh()
    stdscr.getch()


# if a string represents a positive integer, returns the integer, otherwise returns None
def parse_pos_int(x: str):
    if not x.isdigit():
        return None
    retval = int(x)
    return retval if retval > 0 else None


def main(stdscr): 
    curses.curs_set(0)
    # read and validate game settings
    if len(sys.argv) != 6:
        print_err('This program takes exactly five arguments', stdscr)
        return
    alg_name = sys.argv[1]
    coords = [parse_pos_int(x) for x in sys.argv[2:]]
    if None in coords:
        print_err(f'Board size and starting postion must be positive, non-zero integers.\n{str(coords)}', stdscr)
        return
    width, height, start_x, start_y = coords
    if width < start_x or height < start_y:
        print_err('Width and height must be greater than start_x and start_y respectively.', stdscr)
        return
    # initialize the game
    board = game.GameBoard(width, height)
    bot = None
    match alg_name:
        case 'greedy':
            bot = algo.Greedy((start_x - 1, start_y - 1), board)
        case 'tunvis':
            bot = algo.TunnelVis((start_x -1, start_y - 1), board)
        case _:
            print_err(f'Unrecognized algorithm: \"{alg_name}"', stdscr)
    # initialize curses and draw the game board
    stdscr.clear()
    stdscr.addstr(f"{'-' * (width + 2)}\n\r")
    for i in range(height - 1):
        stdscr.addstr(f'|{" " * width}|\n\r')
    stdscr.addstr('-' * (width + 2))
    stdscr.refresh()
    # run the game
    while True:
        updated = bot.run()
        board.display(stdscr)
        if not updated:
            break
        time.sleep(0.001)
    # display exit message
    stdscr.addstr("\n\n\rSimulation finished. Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

if __name__ == '__main__':
    curses.wrapper(main)
