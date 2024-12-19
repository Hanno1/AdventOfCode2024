import helperfunction as hc
from collections import defaultdict
from enum import Enum

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    
NEW_DIRECTION = {Direction.UP: Direction.RIGHT, 
                 Direction.RIGHT: Direction.DOWN, 
                 Direction.DOWN: Direction.LEFT, 
                 Direction.LEFT: Direction.UP}

def read_data():
    data = hc.read_file_line("input")
    return [[char for char in list(line)] for line in data]

def move_guard(position, direction, matrix):
    fields = set()
    row, col = position
    done = False
    while True:
        row += direction.value[0]
        col += direction.value[1]
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            done = True
            break
        if matrix[row][col] == "#":
            break
        fields.add((row, col))
    row -= direction.value[0]
    col -= direction.value[1]
    return done, fields, (row, col), NEW_DIRECTION[direction]

def task1():
    matrix = read_data()
    guard_position = None
    direction = Direction.UP
    for row, line in enumerate(matrix):
        for col, char in enumerate(line):
            if char == "^":
                guard_position = (row, col)
                break
    positions = set()
    positions.add(guard_position)
    done = False
    while not done:
        done, fields, guard_position, direction = move_guard(guard_position, direction, matrix)
        positions.update(fields)
    print(len(positions))
    
def task2():
    matrix = read_data()
    guard_position = None
    start_pos = None
    direction = Direction.UP
    for row, line in enumerate(matrix):
        for col, char in enumerate(line):
            if char == "^":
                guard_position = (row, col)
                start_pos = (row, col)
                break
    positions = set()
    positions.add(guard_position)
    done = False
    while not done:
        done, fields, guard_position, direction = move_guard(guard_position, direction, matrix)
        positions.update(fields)
    positions.remove(start_pos)
    
    counter = 0
    possible_obstacles = []
    for index, (r, c) in enumerate(positions):
        print(index)
        matrix[r][c] = "#"
        current_values = [(start_pos, Direction.UP)]
        current_values = {
            Direction.UP: [(start_pos)],
            Direction.DOWN: [],
            Direction.LEFT: [],
            Direction.RIGHT: []
        }
        old_direction = Direction.UP
        direction = Direction.UP
        guard_position = start_pos
        done = False
        fields = set()
        while not done:
            done, fields, guard_position, direction = move_guard(guard_position, direction, matrix)
            if done:
                break
            for el1, el2 in fields:
                # if ((el1, el2), old_direction) in current_values:
                if (el1, el2) in current_values[old_direction]:                 
                    done = True
                    counter += 1
                    possible_obstacles.append((r, c))
                    break
                # current_values.append(((el1, el2), old_direction))
                current_values[old_direction].append((el1, el2))
            old_direction = direction
        matrix[r][c] = "."
    
    print(start_pos)
    print(counter)
    print(possible_obstacles)
    
task2()