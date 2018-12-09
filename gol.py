#!/usr/bin/env python3
from random import randint
from time import sleep
import curses
import sys


def check_surroundings(x, y, arr, h, w):
    c = '\u2588'
    neighbors = 0
    if y - 1 >= 0 and arr[y - 1][x] == c:
        neighbors += 1
    elif y - 1 < 0 and arr[h - 1][x]:
        neighbors += 1

    if y + 1 < h and arr[y + 1][x] == c:
        neighbors += 1
    elif y + 1 >= h and arr[0][x]:
        neighbors += 1

    if x - 1 >= 0 and arr[y][x - 1] == c:
        neighbors += 1
    elif x - 1 < 0 and arr[y][w - 1]:
        neighbors += 1

    if x + 1 < w and arr[y][x + 1] == c:
        neighbors += 1
    elif x + 1 >= w and arr[y][0]:
        neighbors += 1

    if x - 1 >= 0 and y - 1 >= 0 and arr[y - 1][x - 1] == c:
        neighbors += 1
    elif x - 1 < 0 and y - 1 >= 0 and arr[y - 1][w - 1]:
        neighbors += 1
    elif x - 1 >= 0 and y - 1 < 0 and arr[h - 1][x - 1]:
        neighbors += 1
    elif x - 1 < 0 and y - 1 < 0 and arr[h - 1][w - 1]:
        neighbors += 1

    if x + 1 < w and y + 1 < h and arr[y + 1][x + 1] == c:
        neighbors += 1
    elif x + 1 >= w and y + 1 < h and arr[y + 1][0] == c:
        neighbors += 1
    elif x + 1 < w and y + 1 >= h and arr[0][x + 1] == c:
        neighbors += 1
    elif x + 1 >= w and y + 1 >= h and arr[0][0]:
        neighbors += 1

    if x + 1 < w and y - 1 >= 0 and arr[y - 1][x + 1] == c:
        neighbors += 1
    elif x + 1 >= w and y - 1 >= 0 and arr[y - 1][0] == c:
        neighbors += 1
    elif x + 1 < w and y - 1 < 0 and arr[h - 1][x + 1] == c:
        neighbors += 1
    elif x + 1 >= w and y - 1 < 0 and arr[h - 1][0] == c:
        neighbors += 1

    if x - 1 >= 0 and y + 1 < h and arr[y + 1][x - 1] == c:
        neighbors += 1
    elif x - 1 < 0 and y + 1 >= h and arr[0][w - 1] == c:
        neighbors += 1
    elif x - 1 >= 0 and y + 1 >= h and arr[0][x - 1] == c:
        neighbors += 1
    elif x - 1 < 0 and y + 1 < h and arr[y + 1][w - 1] == c:
        neighbors += 1

    return neighbors


def update_cell(x, y, arr, h, w):
    state = arr[y][x]
    neighbors = check_surroundings(x, y, arr, h, w)
    if neighbors < 2 and arr[y][x] == '\u2588':
        state = ' '
    elif neighbors > 3:
        state = ' '
    elif arr[y][x] == ' ' and neighbors == 3:
        state = '\u2588'
    return state


def random_start(arr,h,w):
    for y in range(h):
        for x in range(w):
            arr[y][x] = '\u2588' if randint(1,6) == 5 else ' '


def main(screen):
    # terminal dimensions
    h = curses.LINES - 1
    w = curses.COLS - 1

    curses.curs_set(0)
    screen.nodelay(True)
    screen.clear()

    s1 = [[' ' for x in range(w)] for y in range(h)]
    s2 = [[' ' for x in range(w)] for y in range(h)]
    current = 0

    # char to print for a live cell
    c = '\u2588'

    #seed the first round
    random_start(s1,h,w)
    for y in range(h):
        for x in range(w):
            s2[y][x] = update_cell(x, y, s1, h, w)
    for y in range(h):
        for x in range(w):
            s1[y][x] = s2[y][x]


    while True:
        inp = screen.getch()
        curses.flushinp()
        if inp == 113:
            sys.exit(0)

        screen.erase()
        for y in range(h):
            for x in range(w):
                s2[y][x] = update_cell(x, y, s1, h, w)

        for y in range(h):
            screen.addstr(y, 0, ''.join(s1[y]))
        screen.refresh()
        sleep(0.1)
        for y in range(h):
            for x in range(w):
                s1[y][x] = s2[y][x]

        current = abs(current - 1)

if __name__ == '__main__':
    curses.wrapper(main)
