import helperfunction as hc

def read_data():
    data = hc.read_file_line("input")
    new_data = []
    for line in data:
        el1, el2 = line.split(":")  
        el2 = el2.strip()
        new_data.append((int(el1), [int(x) for x in el2.split(" ")]))
    return new_data

def try_solving(result, current_number, rest_numbers):
    if len(rest_numbers) == 0:
        return result == current_number
    r1 = try_solving(result, current_number + rest_numbers[0], rest_numbers[1:])
    r2 = try_solving(result, current_number * rest_numbers[0], rest_numbers[1:])
    r3 = try_solving(result, int(str(current_number) + str(rest_numbers[0])), rest_numbers[1:])
    return r1 or r2 or r3

def task1():
    data = read_data()
    total = 0
    for result, numbers in data:
        res = try_solving(result, 0, numbers)
        if res:
            total += result
    print(total)
    
task1()