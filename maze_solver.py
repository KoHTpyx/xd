import sys

error_count = 0

def handle_error():
    global error_count
    error_count += 1
    if error_count == 3:
        print("Перавышана дапушчальная колькасць памылак. Праграма будзе завершана.")
        sys.exit()

def get_start_position(rows, cols):
    while True:
        try:
            start_row = int(input("Увядзіце пачатковы радок: "))
            start_col = int(input("Увядзіце пачатковы слупок: "))
            if not (0 <= start_row < rows and 0 <= start_col < cols):
                raise ValueError
            return start_row, start_col
        except ValueError:
            print("Няправільны ўвод пачатковай пазіцыі")
            handle_error()

def isValidMove(position, rows, cols):
    row, col = position
    return 0 <= row < rows and 0 <= col < cols

def get_neighbors(position, maze):
    row, col = position
    neighbors = []
    
    possible_neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    
    for neighbor in possible_neighbors:
        n_row, n_col = neighbor
        
        if 0 <= n_row < len(maze) and 0 <= n_col < len(maze[0]):
            if maze[n_row][n_col] == 1:
                neighbors.append(neighbor)
    
    return neighbors

def shortest_path(maze, start):
    rows = len(maze)
    cols = len(maze[0])

    shortest_distances = [[sys.maxsize] * cols for _ in range(rows)]
    shortest_distances[start[0]][start[1]] = 0

    queue = [start]

    while queue:
        current = queue.pop(0)

        for neighbor in get_neighbors(current, maze):
            if isValidMove(neighbor, rows, cols) and maze[neighbor[0]][neighbor[1]] == 1:
                if shortest_distances[neighbor[0]][neighbor[1]] == sys.maxsize:
                    shortest_distances[neighbor[0]][neighbor[1]] = shortest_distances[current[0]][current[1]] + 1
                    queue.append(neighbor)

    return shortest_distances

def print_directions(shortest_distances, maze):
    rows = len(shortest_distances)
    cols = len(shortest_distances[0])

    for row in range(rows):
        for col in range(cols):
            position = (row, col)
            distance = shortest_distances[row][col]

            if distance == sys.maxsize:
                print(f"Пазіцыя {position}: недасяжна")
            elif distance == 0:
                print(f"Пазіцыя {position}: стартавая пазіцыя")
            else:
                path = []
                current = position
                while distance > 0:
                    for neighbor in get_neighbors(current, maze):
                        if isValidMove(neighbor, rows, cols) and shortest_distances[neighbor[0]][neighbor[1]] == distance - 1:
                            path.append(neighbor)
                            current = neighbor
                            distance -= 1
                            break
                path.reverse()
                directions = ' -> '.join([f"({pos[0]}, {pos[1]})" for pos in path])
                steps = len(path)
                if steps % 10 == 1 and steps != 11:
                    print(f"Пазіцыя {position}: рухайцеся {directions} ({steps} крок)")
                elif 2 <= steps % 10 <= 4 and (steps < 10 or steps > 20):
                    print(f"Пазіцыя {position}: рухайцеся {directions} ({steps} крокі)")
                else:
                    print(f"Пазіцыя {position}: рухайцеся {directions} ({steps} крокаў)")
