import helperfunction as hc
from enum import Enum
from functools import cache
import copy

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    
POSSIBLE_DIRECTIONS = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]

def preprocess_data():
    data = hc.read_file_line("input")
    data = [[x for x in list(line)] for line in data]
    start, end = None, None
    for row in range(len(data)):
        for col in range(len(data[row])):
            if data[row][col] == "S":
                start = (row, col)
            elif data[row][col] == "E":
                end = (row, col)
    return data, start, end

def print_data(data, cheat=None):
    print("-" * 20)
    new_data = copy.deepcopy(data)
    if cheat:
        cheat1_row, cheat1_col = cheat[0]
        cheat2_row, cheat2_col = cheat[1]
        new_data[cheat1_row][cheat1_col] = "1"
        new_data[cheat2_row][cheat2_col] = "2"
    for line in new_data:
        print("".join(line))

def solve(position):
    mapping[position] = 0
    length = 0
    while position != end:
        row, col = position
        possible_positions = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        length += 1
        for new_row, new_col in possible_positions:
            if data[new_row][new_col] == "#" or (new_row, new_col) in mapping:
                continue
            mapping[(new_row, new_col)] = length
            break
        position = (new_row, new_col)
    return length

def test_path(position, max_length):
    row, col = position
    current_length = mapping[position]
    for direction in POSSIBLE_DIRECTIONS:
        fr, sr = row + direction.value[0], col + direction.value[1]
        if data[fr][sr] != "#":
            continue
        new_row, new_col = fr + direction.value[0], sr + direction.value[1]
        if (new_row, new_col) not in mapping:
            continue
        new_length = mapping[(new_row, new_col)] + (max_length - current_length) + 2
        if new_length < max_length:
            dif = max_length - new_length
            if dif in cheats:
                cheats[dif] += 1
            else:
                cheats[dif] = 1
      
def test_path2(position, max_length):
    row, col = position
    current_length = mapping[position]
    for new_position in mapping:
        dif = abs(row - new_position[0]) + abs(col - new_position[1])
        if dif > 20:
            continue
        new_length = mapping[new_position] + (max_length - current_length) + dif
        if new_length < max_length:
            dif = max_length - new_length
            if dif in cheats:
                cheats[dif] += 1
            else:
                cheats[dif] = 1

def task1():
    global data, end, mapping, cheats
    cheats = dict()
    mapping = dict()
    data, start, end = preprocess_data()
    path_length = solve(start)
    for key in mapping:
        mapping[key] = path_length - mapping[key]
    for key in mapping:
        test_path(key, path_length)
    total = 0
    for key in cheats:
        if key >= 100:
            total += cheats[key]
    print(total)
    
def task2():
    global data, end, mapping, cheats
    cheats = dict()
    mapping = dict()
    data, start, end = preprocess_data()
    path_length = solve(start)
    for key in mapping:
        mapping[key] = path_length - mapping[key]
    c = 0
    print(path_length)
    for key in mapping:
        if c % 100 == 0:
            print(c)
        test_path2(key, path_length)
        c += 1
    total = 0
    for key in cheats:
        if key >= 50:
            print(key, cheats[key])
            total += cheats[key]
    print(total)
    # print(cheats)
    
    # too low 872420
    
task2()