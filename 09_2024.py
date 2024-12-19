import helperfunction as hc

def preprocess_data():
    data = hc.read_file("input")
    line = []
    for i in range(0, len(data) - 1, 2):
        for _ in range(int(data[i])):
            line.append(i // 2)
        for _ in range(int(data[i+1])):
            line.append(".")
    if len(data) % 2 == 1:
        for _ in range(int(data[-1])):
            line.append(len(data) // 2)
    return line

def task1():
    data = preprocess_data()
    start_index = 0
    total = 0
    end_index = len(data) - 1
    result = []
    while end_index >= start_index:
        if data[start_index] != ".":
            total += data[start_index] * start_index
            result.append(data[start_index])
            start_index += 1
        else:
            # gap
            while data[end_index] == ".":
                end_index -= 1
            total += data[end_index] * start_index
            result.append(data[end_index])
            start_index += 1
            end_index -= 1
    print(total)
    
def get_gaps(data):
    gaps = []
    gap_count = 0
    for i in range(len(data)):
        if data[i] != ".":
            if gap_count > 0:
                gaps.append((i - gap_count, gap_count))
                gap_count = 0
        else:
            gap_count += 1
    return gaps

def task2():
    data = preprocess_data()
    gaps = get_gaps(data)
    idx = len(data) - 1
    numbers = set()
    while idx > 0:
        # get current block:
        block_length = 0
        current_number = data[idx]
        print(current_number)
        while data[idx] == current_number:
            block_length += 1
            idx -= 1
        if current_number in numbers:
            while data[idx] == ".":
                idx -= 1
            continue
        for gap_idx, gap_length in gaps:
            if gap_idx >= idx:
                break
            if gap_length >= block_length:
                # data[gap_idx:gap_idx+block_length] = [current_number] * block_length
                for i in range(1, block_length + 1):
                    data[idx + i] = "."
                    data[gap_idx + i - 1] = current_number
                gaps = get_gaps(data)
                break
        while data[idx] == ".":
            idx -= 1
        numbers.add(current_number)
        # print(current_number, data)
        # break
    total = 0
    for index, el in enumerate(data):
        if el != ".":
            total += el * index
    print(total)
task2()