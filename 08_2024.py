import helperfunction as hc

def preprocess_data():
    data = hc.read_file_line("input")
    height, width = len(data), len(data[0])
    antennas = dict()
    for row_index, row in enumerate(data):
        for col_index, col in enumerate(row):
            if col != ".":
                if col in antennas:
                    antennas[col].append((row_index, col_index))
                else:
                    antennas[col] = [(row_index, col_index)]
    return height, width, antennas

def compute_antinodes(positions, height, width):
    antinodes = set()
    for i in range(len(positions)):
        r1, c1 = positions[i]
        for j in range(i + 1, len(positions)):
            r2, c2 = positions[j]
            dx = r1 - r2
            dy = c2 - c1
            node1 = (r1 + dx, c1 - dy)
            node2 = (r2 - dx, c2 + dy)
            if 0 <= node1[0] < height and 0 <= node1[1] < width:
                antinodes.add(node1)
            if 0 <= node2[0] < height and 0 <= node2[1] < width:
                antinodes.add(node2)
    return antinodes

def get_antinodes_in_direction(r, x, dx, dy, height, width):
    antinodes = set()
    while 0 <= r < height and 0 <= x < width:
        antinodes.add((r, x))
        r += dx
        x += dy
    return antinodes

def compute_antinodes2(positions, height, width):
    antinodes = set()
    for i in range(len(positions)):
        r1, c1 = positions[i]
        for j in range(i + 1, len(positions)):
            r2, c2 = positions[j]
            dx = r1 - r2
            dy = c2 - c1
            antinodes.update(get_antinodes_in_direction(r1, c1, dx, -dy, height, width))
            antinodes.update(get_antinodes_in_direction(r2, c2, -dx, dy, height, width))
    return antinodes

def print_antennas(width, height, antennas, antinodes):
    matrix = [["." for _ in range(width)] for _ in range(height)]
    for node in antinodes:
        matrix[node[0]][node[1]] = "#"
    for key in antennas:
        for node in antennas[key]:
            matrix[node[0]][node[1]] = key
    for row in matrix:
        print("".join(row))

def task1():
    height, width, antennas = preprocess_data()
    antinodes = set()
    for key in antennas:
        res = compute_antinodes(antennas[key], height, width)
        antinodes.update(res)
    print(len(antinodes))
    
def task2():
    height, width, antennas = preprocess_data()
    antinodes = set()
    for key in antennas:
        res = compute_antinodes2(antennas[key], height, width)
        antinodes.update(res)
    print_antennas(width, height, antennas, antinodes)
    print(len(antinodes))
    
task2()