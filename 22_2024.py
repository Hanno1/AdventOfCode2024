import helperfunction as hc
from functools import cache

def preprocess_data():
    data = hc.read_file_line("input")
    return [int(line) for line in data]

@cache
def mix_numbers(a, b):
    return a ^ b

@cache 
def prune_number(a):
    return a % 16777216

@cache
def get_new_number(a):
    b = a * 64
    a = mix_numbers(a, b)
    a = prune_number(a)
    
    b = a // 32
    a = mix_numbers(a, b)
    a = prune_number(a)
    
    b = a * 2048
    a = mix_numbers(a, b)
    a = prune_number(a)
    
    return a

def task1():
    data = preprocess_data()
    rounds = 2_000
    for _ in range(rounds):
        for idx, line in enumerate(data):
            data[idx] = get_new_number(line)
    print(sum(data))
    
def task2():
    data = preprocess_data()
    rounds = 2_000
    difs_sums = dict()
    for line in data:
        current_difs = []
        processed_difs = set()
        old_price = line % 10
        line = get_new_number(line)
        new_price = line % 10
        current_difs.append(new_price - old_price)
        old_price = new_price
        for _ in range(3):
            line = get_new_number(line)
            new_price = line % 10
            current_difs.append(new_price - old_price)
            old_price = new_price
        processed_difs.add(tuple(current_difs))
        if tuple(current_difs) in difs_sums:
            difs_sums[tuple(current_difs)] += new_price
        else:
            difs_sums[tuple(current_difs)] = new_price
        for _ in range(rounds - 4):
            line = get_new_number(line)
            new_price = line % 10
            current_difs.append(new_price - old_price)
            current_difs.pop(0)
            old_price = new_price
            if tuple(current_difs) in processed_difs:
                continue
            processed_difs.add(tuple(current_difs))
            if tuple(current_difs) in difs_sums:
                difs_sums[tuple(current_difs)] += new_price
            else:
                difs_sums[tuple(current_difs)] = new_price
    # print(difs_sums)
    max_value = 0
    max_key = None
    for key, value in difs_sums.items():
        if value > max_value:
            max_value = value
            max_key = key
    print(max_value)
    print(max_key)
    
    # 1687 - too low
            
# task1()
task2()