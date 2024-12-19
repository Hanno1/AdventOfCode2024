import helperfunction as hc
from enum import Enum

WIDTH = 71
HEIGHT = 71
TURNS = 1024

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    
DIRECTIONS = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]

def preprocess_data():
    data = hc.read_file_line("input")
    return [(int(y), int(x)) for line in data for x, y in [line.split(",")]]

def print_(walls, path=None):
    data = [["." for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for x, y in walls:
        data[x][y] = "#"
    if path:
        for x, y in path:
            data[x][y] = "O"
    for line in data:
        print("".join(line))
        
def search_path(walls):
    queue = []
    # position
    queue.append((0, 0))
    visited_places = set()
    end = (WIDTH - 1, HEIGHT - 1)
    score = 0
    while len(queue) > 0:
        new_queue = []
        for row, col in queue:
            for direction in DIRECTIONS:
                new_row = row + direction.value[0]
                new_col = col + direction.value[1]
                if new_row < 0 or new_row >= HEIGHT or new_col < 0 or new_col >= WIDTH:
                    continue
                if (new_row, new_col) in visited_places:
                    continue
                if (new_row, new_col) in walls:
                    continue
                if (new_row, new_col) == end:
                    return score + 1
                new_queue.append((new_row, new_col))
                visited_places.add((new_row, new_col))
        queue = new_queue
        score += 1
    return False

def task1():
    data = preprocess_data()
    res = search_path(data[:TURNS])
    print(res)
        
def task2():
    data = preprocess_data()
    turns = 2855
    while turns <= len(data):
        print(f"turns: {turns}")
        walls = data[:turns]
        res = search_path(walls)
        if res == False:
            print(walls[-1])
            break
        turns += 1
    
task2()

