import helperfunction as hc
from functools import cache

def preprocess_data():
    data = hc.read_file_line("input")
    return [[int(x) for x in list(line)] for line in data]

@cache
def find_path(position, number):
    end_positions = set()
    if number == 9:
        end_positions.add(position)
        return end_positions
    row, col = position
    possible_paths = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    for pos in possible_paths:
        r, c = pos
        # check if out of bounds
        if r < 0 or r >= len(data) or c < 0 or c >= len(data[0]):
            continue
        # check number
        if data[r][c] == number + 1:
            end_positions.update(find_path(pos, number + 1))
    return end_positions

# @cache
def find_path2(position, number):
    if number == 9:
        return 1
    row, col = position
    possible_paths = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    total = 0
    for pos in possible_paths:
        r, c = pos
        # check if out of bounds
        if r < 0 or r >= len(data) or c < 0 or c >= len(data[0]):
            continue
        # check number
        if data[r][c] == number + 1:
            total += find_path2(pos, number + 1)
    return total

def task1():
    global data
    data = preprocess_data()
    possible_heads = set()
    for row, line in enumerate(data):
        for col, cell in enumerate(line):
            if cell == 0:
                possible_heads.add((row, col))
    score = 0
    for starting_position in possible_heads:
        res = find_path(starting_position, 0)
        # print(res)
        score += len(res)
    print(score)
    
def task2():
    global data
    data = preprocess_data()
    possible_heads = set()
    for row, line in enumerate(data):
        for col, cell in enumerate(line):
            if cell == 0:
                possible_heads.add((row, col))
    score = 0
    for starting_position in possible_heads:
        res = find_path2(starting_position, 0)
        # print(res)
        score += res
    print(score)
    
task2()