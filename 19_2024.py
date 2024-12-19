import helperfunction as hc
from functools import cache

def preprocess_data():
    data = hc.read_file_line("input")
    towls = data[0].split(", ")
    t = dict()
    for towl in towls:
        if towl[0] not in t:
            t[towl[0]] = []
        t[towl[0]].append(towl)
    tests = data[2:]
    return t, tests

@cache
def solve_line(rest_line):
    first_char = rest_line[0]
    if first_char not in towls:
        return False
    possible_towls = towls[first_char]
    for towl in possible_towls:
        if rest_line.startswith(towl):
            if len(rest_line) == len(towl):
                return True
            else:
                if solve_line(rest_line[len(towl):]):
                    return True
    return False

@cache
def solve_line2(rest_line):
    first_char = rest_line[0]
    if first_char not in towls:
        return 0
    possible_towls = towls[first_char]
    total = 0
    for towl in possible_towls:
        if rest_line.startswith(towl):
            if len(rest_line) == len(towl):
                total += 1
            else:
                total += solve_line2(rest_line[len(towl):])
    return total

def task1():
    global towls
    towls, lines = preprocess_data()
    total = 0
    for line in lines:
        total += solve_line(line)
    print(total)
    
def task2():
    global towls
    towls, lines = preprocess_data()
    total = 0
    for line in lines:
        total += solve_line2(line)
    print(total)
    
task2()