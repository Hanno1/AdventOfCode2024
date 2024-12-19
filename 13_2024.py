import helperfunction as hc

def preprocess_data(task2=False):
    data = hc.read_file_line("input")
    actual_data = []
    actual_line = dict()
    for idx, line in enumerate(data):
        if idx % 4 == 3:
            actual_data.append(actual_line)
            actual_line = dict()
            continue
        split_line = line.split(":")
        content = split_line[1].split(",")
        if idx % 4 == 0 or idx % 4 == 1:
            a_x = int(content[0].split("+")[1])
            a_y = int(content[1].split("+")[1])
            actual_line["a" if idx % 4 == 0 else "b"] = (a_x, a_y)
        else:
            c_x = int(content[0].split("=")[1]) + 10000000000000 if task2 else int(content[0].split("=")[1])
            c_y = int(content[1].split("=")[1]) + 10000000000000 if task2 else int(content[1].split("=")[1])
            actual_line["c"] = (c_x, c_y)
    actual_data.append(actual_line)
    return actual_data

def test_manual(c_x, c_y, a_x, a_y, b_x, b_y): 
    for b in range(100, -1, -1):
        x_val = b * b_x
        y_val = b * b_y
        delta_x = c_x - x_val
        delta_y = c_y - y_val
        if delta_x > 0 and delta_y > 0:
            if delta_x % a_x == 0 and delta_y % a_y == 0:
                a = delta_x // a_x
                if a == delta_y // a_y:
                    return a, b
    return -1, -1

def test_trivial(c_x, c_y, a_x, a_y, b_x, b_y):
    b = (c_y * a_x - a_y * c_x) / (b_y * a_x - a_y * b_x)
    a = (c_x - b * b_x) / a_x
    a = round(a)
    b = round(b)
    if a * a_x + b * b_x == c_x and a * a_y + b * b_y == c_y and a >= 0 and b >= 0:
        return a, b
    return -1, -1

def task1():
    data = preprocess_data()
    total_tokens = 0
    for line in data:
        a, b = test_manual(line["c"][0], line["c"][1], line["a"][0], line["a"][1], line["b"][0], line["b"][1])
        if (a != -1 and b != -1) and (0 <= a <= 100 and 0 <= b <= 100):
            total_tokens += 3 * a + b
    print(total_tokens)
    
def task2():
    data = preprocess_data(task2=True)
    total_tokens = 0
    for line in data:
        a, b = test_trivial(line["c"][0], line["c"][1], line["a"][0], line["a"][1], line["b"][0], line["b"][1])
        if a != -1 and b != -1:
            total_tokens += 3 * a + b
    print(total_tokens)
    
task2()
                        
        