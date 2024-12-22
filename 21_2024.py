import helperfunction as hc
from itertools import pairwise, permutations
from functools import cache

numeric_keypad = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    [None, "0", "A"]
]

NUMERIC_KEYPAD_INDEX = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2)
}

directional_keypad = [
    [None, "^", "A"],
    ["<", "v", ">"],
]

DIRECTIONAL_KEYPAD_INDEX = {
    "^": (0, 1),
    "A": (0, 2),
    "<": (1, 0),
    "v": (1, 1),
    ">": (1, 2)
}

DIRECTION_MAPPING = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

def preprocess_data():
    data = hc.read_file_line("input")
    return [[c for c in list(line)] for line in data]

KEYPAD_DIR = ["^", "v", "<", ">", "A"]

@cache
def get_deltas(a, b):
    if a == b:
        return 0, 0
    if a in KEYPAD_DIR and b in KEYPAD_DIR:
        keypad_mapping = DIRECTIONAL_KEYPAD_INDEX
    else:
        keypad_mapping = NUMERIC_KEYPAD_INDEX
    a_pos = keypad_mapping[a]
    b_pos = keypad_mapping[b]
    drow = b_pos[1] - a_pos[1]
    dcol = b_pos[0] - a_pos[0]
    return drow, dcol

@cache
def is_valid_path(a, b, path):
    if a in KEYPAD_DIR and b in KEYPAD_DIR:
        keypad = directional_keypad
        keypad_mapping = DIRECTIONAL_KEYPAD_INDEX
    else:
        keypad = numeric_keypad
        keypad_mapping = NUMERIC_KEYPAD_INDEX
    row, col = keypad_mapping[a]
    for key in path:
        row += DIRECTION_MAPPING[key][0]
        col += DIRECTION_MAPPING[key][1]
        if keypad[row][col] is None:
            return False
    return True

@cache
def get_all_paths(a, b):
    dx, dy = get_deltas(a, b)
    cx = "<" if dx < 0 else ">"
    cy = "^" if dy < 0 else "v"
    nx = cx * abs(dx) + cy * abs(dy)
    possible = []
    for p in permutations(nx):
        if is_valid_path(a, b, p):
            possible.append("".join(p) + "A")
    return possible

@cache
def get_min_cost(sequence, depth):
    sequence = "A" + sequence
    res = 0
    for a, b in pairwise(sequence):
        paths = get_all_paths(a, b)
        if depth == 0:
            res += min(len(p) for p in paths)
        else:
            res += min(get_min_cost(p, depth - 1) for p in paths)
    return res

def task1():
    data = preprocess_data()
    total = 0
    for row in data:
        total += get_min_cost("".join(row), 2) * int("".join(row[:-1]))
    print(total)

def task2():
    data = preprocess_data()
    total = 0
    for row in data:
        total += get_min_cost("".join(row), 25) * int("".join(row[:-1]))
    print(total)
    
task1()