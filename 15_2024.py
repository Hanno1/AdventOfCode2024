import helperfunction as hc
import enum
import copy


class Direction(enum.Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    
HOZIZONTAL = [Direction.LEFT, Direction.RIGHT]
VERTICAL = [Direction.UP, Direction.DOWN]
    
MOVES_MAPPING = {
    Direction.UP: "^",
    Direction.DOWN: "v",
    Direction.LEFT: "<",
    Direction.RIGHT: ">"
}

MOVES_MAPPING_REVERSE = {
    "^": Direction.UP,
    "v": Direction.DOWN,
    "<": Direction.LEFT,
    ">": Direction.RIGHT
}

MAPPIN_TASK2 = {
    "#": ["#", "#"],
    "O": ["[", "]"],
    ".": [".", "."],
    "@": ["@", "."]
}

def preprocess_data():
    data = hc.read_file_line('input')
    new_data = []
    moves = []
    switch = False
    for line in data:
        print(line)
        if line == '':
            switch = True
            continue
        if not switch:
            new_data += [[el for el in list(line)]]
        else:
            for move in line:
                moves.append(MOVES_MAPPING_REVERSE[move])
    return new_data, moves

def after_pre_process_data(data):
    new_data = []
    for line in data:
        new_line = []
        for el in line:
            new_line += MAPPIN_TASK2[el]
        new_data.append(new_line)
    return new_data

def print_(data):
    print("-" * len(data[0]))
    for line in data:
        print("".join(line))
        
def print_moves(moves):
    print("".join([MOVES_MAPPING[move] for move in moves]))
    
def process_move(data, pos, move):
    new_row, new_col = (pos[0] + move.value[0], pos[1] + move.value[1])
    new_row2, new_col2 = (new_row, new_col)        
    while True:
        if data[new_row2][new_col2] == "#":
            break
        if data[new_row2][new_col2] == ".":
            if new_row2 == new_row and new_col2 == new_col:
                data[new_row2][new_col2] = "@"
                data[pos[0]][pos[1]] = "."
                return (new_row2, new_col2)
            data[new_row2][new_col2] = "O"
            data[new_row][new_col] = "@"
            data[pos[0]][pos[1]] = "."
            return (new_row, new_col)
        new_row2 += move.value[0]
        new_col2 += move.value[1] 
    return pos

def task1():
    data, moves = preprocess_data()
    start_pos = None
    for row, line in enumerate(data):
        for col, el in enumerate(line):
            if el == "@":
                start_pos = (row, col)
                break
        if start_pos:
            break
    for move in moves:
        # print("Move: ", MOVES_MAPPING[move])
        start_pos = process_move(data, start_pos, move)
    print_(data)
    total = 0
    for row, line in enumerate(data):
        for col, el in enumerate(line):
            if el == "O":
                total += 100 * row + col
    print(total)
    
def process_horizontal(data, pos, move):
    row = pos[0]
    new_col = pos[1] + move.value[1]
    new_col2 = new_col
    if data[row][new_col2] == "#":
        return pos
    if data[row][new_col2] == ".":
        data[row][new_col2] = "@"
        data[pos[0]][pos[1]] = "."
        return (row, new_col2)
    # we have a box in the way -> check if we can move it
    while True:
        new_col2 += move.value[1]
        if data[row][new_col2] == "#":
            break
        if data[row][new_col2] == ".":
            # move all boxes
            while new_col2 != new_col:
                next_col = new_col2 - move.value[1]
                data[row][new_col2] = data[row][next_col]
                new_col2 = next_col
            data[row][new_col] = "@"
            data[pos[0]][pos[1]] = "."
            return (row, new_col)
    return pos
    
def process_vertical(data, pos, move):
    new_row, new_col = (pos[0] + move.value[0], pos[1] + move.value[1])
    new_row2, new_col2 = (new_row, new_col)
    if data[new_row2][new_col2] == "#":
        return pos
    if data[new_row2][new_col2] == ".":
        data[new_row2][new_col2] = "@"
        data[pos[0]][pos[1]] = "."
        return (new_row2, new_col2)
    # check boxes
    move_boxes = set()
    total_boxes = []
    if data[new_row2][new_col2] == "[":
        move_boxes.add((new_row2, new_col2, new_col2 + 1))
    else:
        move_boxes.add((new_row2, new_col2 - 1, new_col))
    while len(move_boxes) > 0:
        new_move_boxes = set()
        for box in move_boxes:
            box_row = box[0]
            box_col1 = box[1]
            box_col2 = box[2]
            if data[box_row + move.value[0]][box_col1] == "#" or data[box_row + move.value[0]][box_col2] == "#":
                return pos
            # replace old box
            if data[box_row + move.value[0]][box_col1] == "." and data[box_row + move.value[0]][box_col2] == ".":
                # empty space
                pass
            else:
                b1 = data[box_row + move.value[0]][box_col1]
                b2 = data[box_row + move.value[0]][box_col2]
                if b1 == "[" and b2 == "]":
                    new_move_boxes.add((box_row + move.value[0], box_col1, box_col2))
                    continue
                if b1 == "]":
                    new_move_boxes.add((box_row + move.value[0], box_col1 - 1, box_col1))
                if b2 == "[":
                    new_move_boxes.add((box_row + move.value[0], box_col2, box_col2 + 1))
        total_boxes += list(move_boxes)
        move_boxes = new_move_boxes
    total_boxes.reverse()
    for box in total_boxes:
        data[box[0] + move.value[0]][box[1]] = "["
        data[box[0] + move.value[0]][box[2]] = "]"
        data[box[0]][box[1]] = "."
        data[box[0]][box[2]] = "."
    data[new_row][new_col] = "@"
    data[pos[0]][pos[1]] = "."
    return (new_row, new_col)
    
def task2():
    data, moves = preprocess_data()
    data = after_pre_process_data(data)
    
    start_pos = None
    for row, line in enumerate(data):
        for col, el in enumerate(line):
            if el == "@":
                start_pos = (row, col)
                break
        if start_pos:
            break
        
    for move in moves:
        # print("Move: ", MOVES_MAPPING[move])
        if move in HOZIZONTAL:
            start_pos = process_horizontal(data, start_pos, move)
        else:
            start_pos = process_vertical(data, start_pos, move)
    print_(data)
    total = 0
    for row, line in enumerate(data):
        for col, el in enumerate(line):
            if el == "[":
                total += 100 * row + col
    print(total)
    
    
task2()
        