import curses
import os
import random
from curses import wrapper
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", " ", "#", "#", "#", " ", " ", "#", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", "#", " ", "#"],
    ["#", " ", "#", "#", "#", " ", "#", " ", "#", " ", "#", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", " ", " ", "#", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", " ", "#", " ", "#", "#", " ", " ", "#", " ", "#"],
    ["#", " ", " ", " ", "#", " ", " ", " ", " ", " ", " ", " ", "#", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "X", "#"]
]


def make_random_maze(maze_height=10, maze_with=10):
    maze = []
    x = 0
    while x < maze_height:
        y = 0
        line = []
        while y < maze_with:
            if x == 1 and y == 1:
                line.append("O")
            elif x == maze_height - 2 and y == maze_with - 2:
                line.append("X")
            else:
                if x == 0 or x == maze_height - 1 or y == 0 or y == maze_with - 1:
                    line.append("#")
                else:

                    if random.randint(0, 2) == 0:
                        line.append("#")
                    else:
                        line.append(" ")
            y += 1

        maze.append(line)
        x += 1
    return maze


def print_maze(maze, stdscr, path=[]):
    CYAN = curses.color_pair(1)
    RED = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j, "X", RED)
            else:
                stdscr.addstr(i, j, value, CYAN)


def find_start(maze, start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i, j
    return None


def find_path(maze, stdscr):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)

    q = queue.Queue()
    q.put((start_pos, [start_pos]))

    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.05)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        neighbors = find_neighbors(maze, row, col)
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            r, c = neighbor
            if maze[r][c] == "#":
                continue

            new_path = path + [neighbor]
            q.put((neighbor, new_path))
            visited.add(neighbor)
    return maze


def find_neighbors(maze, row, col):
    neighbors = []

    if row > 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):  # DOWN
        neighbors.append((row + 1, col))
    if col > 0:  # LEFT
        neighbors.append((row, col - 1))
    if col < len(maze[0]):  # RIGHT
        neighbors.append((row, col + 1))

    return neighbors


def setup_maze(stdscr):
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)

    find_path(maze, stdscr)
    stdscr.getch()


def main():
    set_maze()
    wrapper(setup_maze)


def set_maze():
    global maze
    random_maze = input('Random maze? (y/n): ')
    if random_maze == 'y':
        size = os.get_terminal_size()
        maze = make_random_maze(size[1] - 2, size[0] - 2)
    return maze


if __name__ == "__main__":
    main()
