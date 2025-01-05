import helperfunction as hc

def preprocess_data():
    data = hc.read_file_line("input")
    new_data = dict()
    for line in data:
        el1, el2 = line.split("-")
        if el1 not in new_data:
            new_data[el1] = set()
        new_data[el1].add(el2)
        if el2 not in new_data:
            new_data[el2] = set()
        new_data[el2].add(el1)
    return new_data

def get_interconnected_component(new_key: set, current_clique: set, possible: set, processed):
    global data
    set_dif = current_clique - data[new_key]
    # cant add element to clique
    if len(set_dif) != 0:
        return current_clique
    current_clique.add(new_key)
    possible = possible.intersection(data[new_key])
    if possible == set():
        return current_clique
    max_length = len(current_clique)
    max_clique = current_clique
    for el in possible:
        if el in processed:
            continue
        new_clique = get_interconnected_component(el, current_clique, possible, processed)
        if len(new_clique) > max_length:
            max_length = len(new_clique)
            max_clique = new_clique
    return max_clique

def task1():
    data = preprocess_data()
    triples = set()
    processed = set()
    for key in data:
        elements = data[key]
        for idx, el in enumerate(elements):
            if el in processed:
                continue
            for idx2 in range(idx+1, len(elements)):
                el2 = elements[idx2]
                if el2 in processed:
                    continue
                if el2 in data[el] and (key[0] == "t" or el[0] == "t" or el2[0] == "t"):
                    triples.add(tuple([key, el, el2]))
        processed.add(key)
    print(len(triples))
    # print(triples)
    
def task2():
    global data
    data = preprocess_data()
    processed = set()
    max_interconnected_component = set()
    max_length = 0
    for key in data:
        component = get_interconnected_component(key, set(), data[key], processed)
        length = len(component)
        if length > max_length:
            max_length = length
            max_interconnected_component = component
        processed.add(key)
    max_interconnected_component = list(max_interconnected_component)
    max_interconnected_component.sort()
    print(max_length, ",".join(max_interconnected_component))
    
task2()