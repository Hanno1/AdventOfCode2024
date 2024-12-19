import helperfunction as hc
from functools import cache

def preprocess_data():
    data = hc.read_file("input")
    return [int(x) for x in data.split(" ")]

@cache
def process_stone(stone):
    if stone == 0:
        return [1]
    if len(str(stone)) % 2 == 0:
        str_stone = str(stone)
        return [int(str_stone[:len(str_stone)//2]), int(str_stone[len(str_stone)//2:])]
    return [stone * 2024]

@cache
def process_round_and_stone(stone, round):
    if round == 0:
        return 1
    new_stones = process_stone(stone)
    total = 0
    for n_stone in new_stones:
        total += process_round_and_stone(n_stone, round-1)
    return total

def task1():
    stones = preprocess_data()
    r = 75
    for round in range(r):
        new_stones = []
        for stone in stones:
            new_stones += process_stone(stone)
        stones = new_stones
    print(len(stones))
    
def task2():
    stones = preprocess_data()
    total = 0
    for stone in stones:
        total += process_round_and_stone(stone, 75)
    print(total)
    
task2()