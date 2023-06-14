import sys
from maze_solver import shortest_path, print_directions
from maze_generator import handle_error, get_maze_size, get_maze

def main():
    maze = []
    error_count = 0

    while True:
        try:
            rows, cols = get_maze_size()
            maze = get_maze(rows, cols)

            while True:
                start_row_input = input("Увядзіце пачатковы радок: ")
                start_col_input = input("Увядзіце пачатковы слупок: ")

                if not start_row_input.isdigit() or not start_col_input.isdigit():
                    raise ValueError("Неправільны ўвод пачатковай пазіцыі")

                start_row = int(start_row_input)
                start_col = int(start_col_input)

                if start_row < 0 or start_row >= rows or start_col < 0 or start_col >= cols:
                    print("Пачатковая пазіцыя ваходзіць за межы лабірынта")
                    handle_error()
                else:
                    if maze[start_row][start_col] == 0:
                        print("Пачатковая пазіцыя не можа быць сцяной")
                        handle_error()
                    else:
                        break

            find_exit = input("Вы хочаце найсці выхад з лабірынта? (да/нет): ").lower() == "да"

            if find_exit:
                while True:
                    exit_row_input = input("Увядзіце канчатковы радок: ")
                    exit_col_input = input("Увядзіце канчатковы слупок: ")

                    if not exit_row_input.isdigit() or not exit_col_input.isdigit():
                        raise ValueError("Неправільны ўвод канчатковай пазіцыі")

                    exit_row = int(exit_row_input)
                    exit_col = int(exit_col_input)

                    if exit_row < 0 or exit_row >= rows or exit_col < 0 or exit_col >= cols:
                        print("Канчатковая пазіцыя ваходзіць за межы лабірынта")
                        handle_error()
                    else:
                        if maze[exit_row][exit_col] == 0:
                            print("Канчатковы пункт выхода является стеной і не можа быць достігнут")
                            handle_error()
                        else:
                            break

                shortest_distances = shortest_path(maze, (start_row, start_col))
                print_directions(shortest_distances, maze, (exit_row, exit_col))
                break
            else:
                shortest_distances = shortest_path(maze, (start_row, start_col))
                print_directions(shortest_distances, maze)
                break
        except ValueError as err:
            print(str(err))
            handle_error()
            error_count += 1
            if error_count == 3:
                print("Перавышана дапушчальная колькасць памылак. Праграма будзе завершана.")
                sys.exit()

if __name__ == "__main__":
    main()