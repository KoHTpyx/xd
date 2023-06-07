import sys
from maze_solver import handle_error

def get_maze_size():
    while True:
        try:
            rows = int(input("Увядзіце колькасць радкоў у лабірынце: "))
            cols = int(input("Увядзіце колькасць слупкоў у лабірынце: "))
            if rows <= 0 or cols <= 0:
                raise ValueError
            return rows, cols
        except ValueError:
            print("Няправільны ўвод радкоў/слупкоў")
            handle_error()

def get_maze(rows, cols):
    maze = []
    print("Увядзіце лабірынт (0 - сцяна, 1 - праход):")
    for _ in range(rows):
        while True:
            try:
                row = list(map(int, input().split()))
                if len(row) != cols:
                    raise ValueError
                maze.append(row)
                break
            except ValueError:
                print("Няправільны ўвод радка лабірынта")
                handle_error()

    return maze
