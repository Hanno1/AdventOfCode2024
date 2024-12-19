import helperfunction as hc

def preprocess_data():
    data = hc.read_file_line("input")
    return [[x for x in list(line)] for line in data]

def get_region(region_char, row, col, region_data):
    possible_new_regions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    edges = 0
    region_data.add((row, col))
    for r, c in possible_new_regions:
        if r >= 0 and c >= 0 and r < len(data) and c < len(data[0]):
            if data[r][c] == region_char and (r, c) not in region_data:
                edgs, region_data = get_region(region_char, r, c, region_data)
                edges += edgs
            elif (r, c) not in region_data:
                edges += 1
        else:
            edges += 1
    return edges, region_data

def process_region(region):
    total_borders = 0
    row_dict = dict()
    min_col = 1_000
    max_col = 0
    max_row = 0
    for row, col in region:
        if row not in row_dict:
            row_dict[row] = []
        row_dict[row].append(col)
        if col < min_col:
            min_col = col
        if col > max_col:
            max_col = col
        if row > max_row:
            max_row = row
    # mode 0: . mode1: . mode2: A mode3: A
    #         .        A        .        A
    row_dict[max_row + 1] = []
    for key in row_dict:
        above = row_dict[key - 1] if key - 1 in row_dict else []
        below = row_dict[key] if key + 1 in row_dict else []
                
        mode = 0
        for c in range(min_col, max_col + 1):
            new_mode =None
            if c in above:
                if c in below:
                    new_mode = 3
                else:
                    new_mode = 2
            else:
                if c in below:
                    new_mode = 1
                else:
                    new_mode = 0
            # compare modes:
            if mode == 0 or mode == 3:
                if new_mode == 1 or new_mode == 2:
                    total_borders += 1
            elif mode == 1:
                if new_mode == 2:
                    total_borders += 1
            else:
                if new_mode == 1:
                    total_borders += 1
                    
            mode = new_mode
    return total_borders
    
def task1():
    global data
    data = preprocess_data()
    processed_regions = set()
    prices = 0
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if (row, col) not in processed_regions:
                borders, region = get_region(char, row, col, set())
                prices += borders * len(region)
                processed_regions.update(region)
    print(prices)
    
def task2():
    global data 
    data = preprocess_data()
    processed_regions = set()
    prices = 0
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if (row, col) not in processed_regions:
                _, region = get_region(char, row, col, set())
                b1 = process_region(region)
                switched_region = set()
                for r, c in region:
                    switched_region.add((c, r))
                b2 = process_region(switched_region)
                price = (b1 + b2) * len(region)
                prices += price
                processed_regions.update(region)
    print(prices)
    
task2()