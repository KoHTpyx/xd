import random
from maze_solver import handle_error

error_count = 0

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

def generate_maze(rows, cols):
    maze = []
    for _ in range(rows):
        row = [random.randint(0, 1) for _ in range(cols)]
        maze.append(row)
    return maze
    

def get_maze(rows, cols):
    print("Вы хочаце самастойна ўвесці лабірынт або згенераваць яго аўтаматычна?")
    while True:
        choice = input("Выберыце варыянт (увядзіце 'самастойна' або 'аўтаматычна'): ")
        if choice == "самастойна":
            print("Увядзіце лабірынт (0 - сцяна, 1 - праход):")
            try:
               return parse_maze_input(rows, cols)
            except ValueError:
                handle_error()
                continue
        elif choice == "аўтаматычна":
            maze = generate_maze(rows, cols)
            print("Сгенерированный лабиринт:")
            for row in maze:
                for cell in row:
                    print(cell, end=' ')
                print()
            return maze
        else:
            print("Неправільны выбар. Калі ласка, паспрабуйце яшчэ раз.")
            handle_error()