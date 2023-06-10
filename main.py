from maze_generator import get_maze_size, get_maze
from maze_solver import get_start_position, shortest_path, print_directions, handle_error

def main():
    rows, cols = get_maze_size()
    maze = get_maze(rows, cols)
    start = get_start_position(maze, rows, cols)

    global error_count
    error_count = 0

    try:
        shortest_distances = shortest_path(maze, start)
        print_directions(shortest_distances, maze)
    except Exception as e:
        print(f"Адбылася памылка: {e}")
        handle_error()

if __name__ == '__main__':
    main()