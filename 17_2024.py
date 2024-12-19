import helperfunction as hc

def preprocess_data():
    data = hc.read_file_line("input")
    instructions = [int(el) for el in data[-1].split(": ")[1].split(",")]
    register_values = data[:3]
    values = [0, 0, 0]
    for index, line in enumerate(register_values):
        values[index] = int(line.split(": ")[1])
    return instructions, values

def get_combo_operand(register_values, instruction_number):
    if instruction_number <= 3:
        return instruction_number
    return register_values[instruction_number - 4]

def process_command(commands, register_values, instruction_pointer):
    command = commands[instruction_pointer]
    number = commands[instruction_pointer + 1]
    output = None
    if command == 0:
        # adv
        numerator = register_values[0]
        denominator = 2**get_combo_operand(register_values, number)
        register_values[0] = numerator // denominator
    elif command == 1:
        register_values[1] = register_values[1] ^ number
    elif command == 2:
        register_values[1] = get_combo_operand(register_values, number) % 8
    elif command == 3:
        if register_values[0] != 0:
            instruction_pointer = number - 2
    elif command == 4:
        register_values[1] = register_values[1] ^ register_values[2]
    elif command == 5:
        output = get_combo_operand(register_values, number) % 8
    elif command == 6:
        numerator = register_values[0]
        denominator = 2**get_combo_operand(register_values, number)
        register_values[1] = numerator // denominator
    else:
        numerator = register_values[0]
        denominator = 2**get_combo_operand(register_values, number)
        register_values[2] = numerator // denominator
    instruction_pointer += 2
    return register_values, instruction_pointer, output

def process_all_commands(commands, register_A, target_value):
    # just have value of register A
    instruction_pointer = 0
    register_values = [register_A, 0, 0]
    while instruction_pointer < len(commands):
        register_values, instruction_pointer, output = process_command(commands, register_values, instruction_pointer)
        if output is not None:
            return output == target_value
    raise Exception("No output found")
        
def task1():
    instr, register_values = preprocess_data()
    instruction_pointer = 0
    total = []
    while instruction_pointer < len(instr):
        register_values, instruction_pointer, output = process_command(instr, register_values, instruction_pointer)
        if output is not None:
            total.append(output)
    print(",".join([str(el) for el in total]))
    # print(register_values, instr)
    
def task2():
    instr, _ = preprocess_data()
    possible_values = [i for i in range(1, 8)]
    for index in range(len(instr) - 1, 0, -1):
        new_possible_values = []
        print(index, possible_values)
        for value in possible_values:
            res = process_all_commands(instr, value, instr[index])
            if res:
                for i in range(8):
                    new_possible_values.append(value * 8 + i)
        possible_values = new_possible_values
    print(possible_values)
    
    for value in possible_values:
        instruction_pointer = 0
        total = []
        register_values = [value, 0, 0]
        while instruction_pointer < len(instr):
            register_values, instruction_pointer, output = process_command(instr, register_values, instruction_pointer)
            if output is not None:
                total.append(output)
        if total == instr:
            print(value)
            break
    
task2()