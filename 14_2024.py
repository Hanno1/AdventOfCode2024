import helperfunction as hc

WIDTH = 101
HEIGHT = 103

def preprocess_data():
    data = hc.read_file_line("input")
    new_data = []
    for line in data:
        line = line.split(" ")
        position = line[0].split("=")[1].split(",")
        velocity = line[1].split("=")[1].split(",")
        new_data.append(((int(position[0]), int(position[1])), (int(velocity[0]), int(velocity[1]))))
    return new_data

def count_positions(data):
    positions = [x[0] for x in data]
    for idx, pos in enumerate(positions):
        if pos in positions[idx+1:]:
            return False
    return True

def print_(data):
    print("".join(["#" for _ in range(WIDTH)]))
    positions = [x[0] for x in data]
    for i in range(HEIGHT):
        line = ""
        for j in range(WIDTH):
            if (j, i) in positions:
                line += str(positions.count((j, i)))
            else:
                line += "."
        print(line)
        
def move_data(data):
    new_data = []
    for d in data:
        col, row = d[0]
        v_right, v_up = d[1]
        new_col, new_row = col + v_right, row + v_up
        new_data.append(((new_col % WIDTH, new_row % HEIGHT), (v_right, v_up)))
    return new_data

def task1():
    data = preprocess_data()
    print_(data)
    for _ in range(100):
        data = move_data(data)
    quadrant_counts = [0, 0, 0, 0]
    half_width = (WIDTH - 1) // 2
    half_height = (HEIGHT - 1) // 2
    positions = [x[0] for x in data]
    for col, row in positions:
        if col == half_width or row == half_height:
            continue
        elif col < half_width:
            if row < half_height:
                quadrant_counts[0] += 1
            else:
                quadrant_counts[2] += 1
        else:
            if row < half_height:
                quadrant_counts[1] += 1
            else:
                quadrant_counts[3] += 1
    count = 1
    for i in range(4):
        count *= quadrant_counts[i]
    print(count)
    
def task2():
    data = preprocess_data()
    print_(data)
    temp = 0
    counter = 0
    while temp < 4:
        counter += 1
        data = move_data(data)
        c = count_positions(data)
        if c:
            print("-----------------" + str(counter) + "-----------------")
            temp += 1
            print_(data)
    
task2()