import helperfunction as hc
from collections import defaultdict

def preprocess_data():
    data = hc.read_file_line("input")
    ordering_rules = []
    pages = []
    
    end_rules = False
    for line in data:
        if line == "":
            end_rules = True
            continue
        if not end_rules:
            el1, el2 = line.split("|")
            ordering_rules.append((int(el1), int(el2)))
        elif end_rules:
            pages.append([int(x) for x in line.split(",")])
            
    return ordering_rules, pages

def create_graph(rules):
    graph = defaultdict(set)
    for n1, n2 in rules:
        graph[n1].add(n2)
        if graph[n2] is None:
            graph[n2] = set()
    return graph

def bfs(graph, node, visited):
    res = set()
    for child in graph[node]:
        if child not in visited:
            visited.add(child)
            result = bfs(graph, child, visited)
            for el in result:
                res.add(el)
            res.add(child)
    return res

def check_line(line, graph_rules):
    for index, el in enumerate(line):
        if el not in graph_rules:
            continue
        nodes = graph_rules[el]
        for j in range(index):
            el = line[j]
            if el in nodes:
                return False
    return True

def reorder_line(line, graph_rules):
    elements_to_sort = line
    new_line = []
    index = 0
    while elements_to_sort:
        el = elements_to_sort[index]
        added = True
        if el not in graph_rules:
            # shouldnt happen, but thats the case that the elemnt is not in the initial graph
            new_line.append(el)
            continue
        for other_el in elements_to_sort:
            nodes = graph_rules[other_el]
            if el in nodes:
                added = False
                break
        if added:
            new_line.append(el)
            elements_to_sort.remove(el)
            index = 0
            continue
        index += 1
    return new_line
            

def task1():
    rules, tasks = preprocess_data()
    print("Data preprocessed")
    graph = create_graph(rules)
    print("Graph created")
        
    bfs_graph = {}
    for key in graph:
        result = bfs(graph, key, set())
        if key in result:
            result.remove(key)
        bfs_graph[key] = result
        
    # print(bfs_graph)
    count = 0
    for task in tasks:
        res = check_line(task, graph)
        if res:
            count += task[(len(task) - 1) // 2]
    print(count)
    # print(graph)
    
def task2():
    rules, tasks = preprocess_data()
    print("Data preprocessed")
    graph = create_graph(rules)
    print("Graph created")
        
    bfs_graph = {}
    for key in graph:
        result = bfs(graph, key, set())
        if key in result:
            result.remove(key)
        bfs_graph[key] = result
        
    count = 0
    for task in tasks:
        res = check_line(task, graph)
        if not res:
            # reorder task
            line = reorder_line(task, graph)
            print(line)
            count += line[(len(line) - 1) // 2]
    print(count)
    
# task1()
task2()