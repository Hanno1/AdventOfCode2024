import helperfunction as hc

TARGET = "mul("
DO_TARGET = "do("
DONT_TARGET = "don't("
NUMBERS = [str(i) for i in range(10)]

def read_data():
    data = hc.read_file("03")
    return data
    
def parse_data(line):
    res = 0
    c = 0
    mode = 0
    number1 = ""
    number2 = ""
    do = True
    print(line)
    for el in line:
        if mode != 0:
            if el == ")":
                if mode == 2 and number2 != "" and do:
                    res += int(number1) * int(number2)
                mode = 0
                number1 = ""
                number2 = ""
            elif el == ",":
               if mode == 1 and number1 != "":
                   mode = 2
            elif el in NUMBERS:
                if mode == 1:
                    number1 += el
                elif mode == 2:
                    number2 += el
            else:
                mode = 0
                number1 = ""
                number2 = ""
            continue
        elif c < len(TARGET) and el == TARGET[c]:
            c += 1
            if c == len(TARGET):
                c = 0
                mode = 1
            continue
        elif c < len(DO_TARGET) and el == DO_TARGET[c]:
            c += 1
            if c == len(DO_TARGET):
                c = 0
                do = True
            continue
        elif c < len(DONT_TARGET) and el == DONT_TARGET[c]:
            c += 1
            if c == len(DONT_TARGET):
                c = 0
                do = False
            continue
        c = 0
        mode = 0
    print(res)
    
d = read_data()
parse_data(d)
    