import sys
from maze_solver import handle_error

error_count = 0

def handle_error():
    global error_count
    error_count += 1
    if error_count == 3:
        print("Перавышана дапушчальная колькасць памылак. Праграма будзе завершана.")
        sys.exit()

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

def parse_maze_input(rows, cols):
    maze = []
    for _ in range(rows):
        while True:
            try:
                row = list(map(int, input().split()))
                if len(row) != cols:
                    raise ValueError
                if any(elem not in [0, 1] for elem in row):
                    raise ValueError
                maze.append(row)
                break
            except ValueError:
                print("Няправільны ўвод радка лабірынта")
                handle_error()
    return maze

def get_maze(rows, cols):
    print("Увядзіце лабірынт (0 - сцяна, 1 - праход):")
    try:
        maze = parse_maze_input(rows, cols)
    except ValueError:
        handle_error()
        return get_maze(rows, cols)
    return maze