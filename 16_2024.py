import helperfunction as hc
import enum

class Direction(enum.Enum):
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    WEST = (0, -1)
    EAST = (0, 1)
    
DIRECTIONS = [Direction.NORTH, Direction.SOUTH, Direction.WEST, Direction.EAST]
DIRECTION_MAP = {
    Direction.NORTH: [Direction.WEST, Direction.EAST, Direction.NORTH],
    Direction.SOUTH: [Direction.EAST, Direction.WEST, Direction.SOUTH],
    Direction.WEST: [Direction.SOUTH, Direction.NORTH, Direction.WEST],
    Direction.EAST: [Direction.NORTH, Direction.SOUTH, Direction.EAST]
}

def preprocess_data():
    data = hc.read_file_line("input")
    walls = dict()
    end = None
    start = None
    for i in range(len(data)):
        walls[i] = set()
        for j in range(len(data[i])):
            if data[i][j] == "#":
                walls[i].add(j)
            elif data[i][j] == "E":
                end = (i, j)
            elif data[i][j] == "S":
                start = (i, j)
    return walls, end, start, len(data), len(data[0])

def print_(walls, end, start, height, width, paths=None):
    data = [["." for _ in range(width)] for _ in range(height)]
    for row_key in walls:
        for col_key in walls[row_key]:
            data[row_key][col_key] = "#"
    data[end[0]][end[1]] = "E"
    data[start[0]][start[1]] = "S"
    
    if paths:
        for path in paths:
            for row, col in path:
                if (row, col) not in walls:
                    data[row][col] = "O"
    
    for row in data:
        print("".join(row))

def solve_BFS(start, direction, walls, end):
    current_path = set()
    current_path.add(start)
    queue = [(start, direction, 0, current_path)]
    lowest_score = float("inf")
    best_path = []
    visited = dict()
    while queue:
        position, direction, score, current_path = queue.pop(0)
        if position == end:
            if score == lowest_score:
                best_path.append(current_path)
            elif score < lowest_score:
                lowest_score = score
                best_path = [current_path]
            continue
        if (position, direction) in visited:
            visited_score = visited[(position, direction)]
            if visited_score < score:
                continue
            if visited_score > score:
                visited[(position, direction)] = score
        else:
            visited[(position, direction)] = score
        possible_directions = DIRECTION_MAP[direction]
        for d in possible_directions:
            score_ = score
            new_row, new_col = position[0] + d.value[0], position[1] + d.value[1]
            if new_col in walls[new_row] or (new_row, new_col) in current_path:
                continue
            if d != direction:
                score_ += 1000
            c = current_path.copy()
            c.add((new_row, new_col))
            queue.append(((new_row, new_col), d, score_ + 1, c))
    return lowest_score, best_path
    
def task1():
    walls, end, start, height, width = preprocess_data()
    # print_(walls, end, start, height, width)
    ls, _, _ = solve_BFS(start, Direction.EAST, walls, end)
    print(ls)
            
def task2():
    walls, end, start, height, width = preprocess_data()
    # print_(walls, end, start, height, width)
    ls, paths = solve_BFS(start, Direction.EAST, walls, end)
    print(ls, paths)
    print_(walls, end, start, height, width, paths)
    # print(solutions)
    all_positions = set()
    for path in paths:
        all_positions.update(path)
        
    print(len(all_positions))
    
task2()