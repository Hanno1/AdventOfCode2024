import helperfunction as hc

def preprocess_data():
    data = hc.read_file_line("02")
    d = [line.split(" ") for line in data]
    new_d = []
    for line in d:
        new_line = []
        for entry in line:
            new_line.append(int(entry))
        new_d.append(new_line)
    return new_d

def test_line(line, damper=0):
    first = line[0]
    second = line[1]
    if first > second:
        line.reverse()
    for i in range(len(line) - 1):
        element = line[i]
        next_element = line[i + 1]
        distance = next_element - element
        if distance < 1 or distance > 3:
            if damper:
                # remove either left or right element of mistake and test again
                new_line1 = line[:i] + line[i + 1:]
                new_line2 = line[:i + 1] + line[i + 2:]
                new_line3 = line[1:]
                new_line4 = line[:-1]
                                
                if test_line(new_line1) or test_line(new_line2) or test_line(new_line3) or test_line(new_line4):
                    return True
                # for j in range(len(line)):
                #     new_line = line[:j] + line[j + 1:]
                #     # print(new_line)
                #     if test_line(new_line):
                #         return True
                return False
            return False
    return True

def task1():
    data = preprocess_data()
    count = 0
    for line in data:
        first = line[0]
        second = line[1]
        res = None
        if first < second:
            res = test_line(line)
        elif first > second:
            line.reverse()
            res = test_line(line)
        if res:
            count += 1
            # print(line)
    print(count)
    
def task2():
    data = preprocess_data()
    count = 0
    result = []
    index = 0
    for line in data:
        res = test_line(line, 1)
        if res:
            count += 1
            result.append(index)
        index += 1
    print(count)
    # hc.write_to_file("282", result)
    # 271 -> too low
    # 326 -> too high
    # 277 -> not correct ???
    # 281 -> not correct ???
    # 282 -> not correct ???
    
task2()
        