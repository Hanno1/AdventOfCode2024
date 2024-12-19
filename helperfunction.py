def read_file(filename):
    with open(f'{filename}.txt') as f:
        content = f.read()
    return content

def read_file_line(filename):
    lines = []
    with open(f'{filename}.txt') as f:
        for line in f.readlines():
            lines.append(line.replace('\n', ''))
    return lines

def write_to_file(filename, data):
    with open(f'{filename}.txt', 'w') as f:
        for line in data:
            if type(line) == list:
                s = " ".join([str(x) for x in line])
            else:
                s = str(line)
            f.write(s + '\n')
