import helperfunction as hc
import enum

class Direction(enum.Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP_LEFT = (-1, -1)
    UP_RIGHT = (-1, 1)
    DOWN_LEFT = (1, -1)
    DOWN_RIGHT = (1, 1)
    
DIRECTIONS = [Direction.UP, 
              Direction.DOWN, 
              Direction.LEFT, 
              Direction.RIGHT, 
              Direction.UP_LEFT, 
              Direction.UP_RIGHT, 
              Direction.DOWN_LEFT, 
              Direction.DOWN_RIGHT]

def read_data():
    data = hc.read_file_line("input")
    new_data = []
    for line in data:
        new_data.append(list(line))
    return new_data

def check_word(data, r, c):
    count = 0
    for direction in DIRECTIONS:
        for i in range(1, 4):
            new_r = r + direction.value[0] * i
            new_c = c + direction.value[1] * i
            if new_r < 0 or new_r >= len(data) or new_c < 0 or new_c >= len(data[0]):
                break
            elif i == 1 and data[new_r][new_c] != "M":
                break
            elif i == 2 and data[new_r][new_c] != "A":
                break
            elif i == 3 and data[new_r][new_c] != "S":
                break
            elif i == 3 and data[new_r][new_c] == "S":
                count += 1
    return count

def check_word2(data, r, c):
    if r < 1 or r >= len(data) - 1 or c < 1 or c >= len(data[0]) - 1:
        return False
    right_els = set([data[r-1][c-1], data[r+1][c+1]])
    if "M" not in right_els or "S" not in right_els:
        return False
    left_els = set([data[r-1][c+1], data[r+1][c-1]])
    if "M" not in left_els or "S" not in left_els:
        return False
    return True

def task1():
    data = read_data()
    count = 0
    for row, line in enumerate(data):
        for col, el in enumerate(line):
            if el == "X":
                count += check_word(data, row, col)
    print(count)
    
def task2():
    data = read_data()
    count = 0
    for row, line in enumerate(data):
        for col, el in enumerate(line):
            if el == "A":
                if check_word2(data, row, col):
                    count += 1
    print(count)
    # too high: 2006
    
task2()