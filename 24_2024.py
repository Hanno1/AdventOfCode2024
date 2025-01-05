import helperfunction as hc
import networkx as nx
import matplotlib.pyplot as plt

def preprocess_data():
    data = hc.read_file_line("input")
    initial_values = dict()
    for idx, line in enumerate(data):
        if line == "":
            break
        gate, value = line.split(": ")
        initial_values[gate] = int(value)
    gates = []
    for i in range(idx+1, len(data)):
        left, out = data[i].split(" -> ")
        in1, operand, in2 = left.split(" ")
        gates.append((operand, in1, in2, out))
    topological_sorting = []
    processed = [key for key in initial_values.keys()]
    while len(topological_sorting) != len(gates):
        for gate in gates:
            _, in1, in2, out = gate
            if in1 in processed and in2 in processed and out not in processed:
                topological_sorting.append(gate)
                processed.append(out)
    return initial_values, topological_sorting

def simulate_circuit(initial_values, gates):
    values = initial_values
    for gate in gates:
        operand, in1, in2, out = gate
        if operand == "AND":
            values[out] = values[in1] & values[in2]
        elif operand == "OR":
            values[out] = values[in1] | values[in2]
        elif operand == "XOR":
            values[out] = 1 if values[in1] != values[in2] else 0
    return values

def get_input_gates(gate, gates):
    current_input_gates = set()
    current_input_gates.add(gate)
    final_input = set()
    while len(current_input_gates) != 0:
        new_input_gates = set()
        for input in current_input_gates:
            if input[0] == "x" or input[0] == "y":
                final_input.add(input)
            for gate in gates:
                _, in1, in2, out = gate
                if out == input:
                    new_input_gates.add(in1)
                    new_input_gates.add(in2)
        current_input_gates = new_input_gates
    return final_input

def get_imediate_input_gates(gate, gates):
    for g in gates:
        op, in1, in2, out = g
        if out == gate:
            return (in1, in2, op)
    return None

def get_formular_print(gate, gates):
    if gate[0] == "x" or gate[0] == "y":
        return gate
    in1, in2, op = get_imediate_input_gates(gate, gates)
    n1 = get_formular_print(in1, gates)
    n2 = get_formular_print(in2, gates)
    return "(" + n1 + " " + op + " " + n2 + ")"

def get_formular(gate, gates):
    if gate[0] == "x" or gate[0] == "y":
        number = int(gate[1:])
        return gate, number
    in1, in2, op = get_imediate_input_gates(gate, gates)
    if in1[0] == "y":
        tmp = in1
        in1 = in2
        in2 = tmp
    n1, d1 = get_formular(in1, gates)
    n2, d2 = get_formular(in2, gates)
    return (op, n1, n2) if d1 >= d2 else (op, n2, n1), min(d1, d2)

def get_full_gate(char, depth):
    if depth < 10:
        return char + "0" + str(depth)
    return char + str(depth)
    
def get_input_gates2(depth):
    gate_number = str(depth) if depth >= 10 else "0" + str(depth)
    return ("x" + gate_number, "y" + gate_number)
    
def check_formular(depth, gates):
    op, n1, n2 = get_formular(get_full_gate("z", depth), gates)[0]
    if depth == 0:
        return op == "XOR" and n1 == "x00" and n2 == "y00", depth
    if op != "XOR":
        return False, depth
    in1, in2 = get_input_gates2(depth)
    op1, n11, n21 = n1
    if op1 != "XOR" or n11 != in1 or n21 != in2:
        return False, depth
    return check_transfer(depth, n2, gates)

def check_transfer(depth, gate, gates):
    op, n1, n2 = gate
    if depth == 1:
        return op == "AND" and n1 == "x00" and n2 == "y00", gate
    if op != "OR":
        return False, gate
    prev1, prev2 = get_input_gates2(depth - 1)
    op1, n11, n21 = n1
    op2, n12, n22 = n2
    if op1 != "AND" or n11 != prev1 or n21 != prev2:
        return False, gate
    if op2 != "AND":
        return False, gate
    op12, n112, n212 = n12
    if op12 != "XOR" or n112 != prev1 or n212 != prev2:
        return False, gate
    return check_transfer(depth - 1, n22, gates)

def generate_formular(depth):
    if depth == 0:
        return ("XOR", "x00", "y00")
    in1, in2 = get_input_gates2(depth)
    return ("XOR", ("XOR", in1, in2), generate_transfer(depth))

def generate_transfer(depth):
    if depth == 1:
        return ("AND", "x00", "y00")
    prev1, prev2 = get_input_gates2(depth - 1)
    return ("OR", ("AND", prev1, prev2), ("AND", ("XOR", prev1, prev2), generate_transfer(depth - 1)))

def task1():
    initial, gates = preprocess_data()
    values = simulate_circuit(initial, gates)
    bits = ""
    z_names = [name for name in values.keys() if name[0] == "z"]
    z_names.sort(reverse=True)
    for name in z_names:
        bits += str(values[name])
    print(int(bits, 2))
    
def task2():
    _, gates = preprocess_data()
    different_gates = set()
    edges = set()
    for op, in1, in2, out in gates:
        different_gates.add((out, op))
        edges.add((in1, out))
        edges.add((in2, out))
        
    G = nx.DiGraph()
    G.add_nodes_from([(g, {"Operation": op}) for g, op in different_gates])
    G.add_nodes_from([get_full_gate("x", i) for i in range(45)])
    G.add_nodes_from([get_full_gate("y", i) for i in range(45)])
    # G.add_nodes_from([get_full_gate("z", i) for i in range(45)])
    G.add_edges_from(edges)
    
    # try:
    #     pos = nx.nx_agraph.graphviz_layout(G, prog="dot")
    # except ImportError:
    #     raise ImportError(
    #         "Graphviz is required for this layout. Ensure you have pygraphviz or pydot installed."
    #     )
    
    plt.figure(figsize=(50, 100))
    nx.draw(
        G,
        with_labels=True,
        node_size=600,
        node_color="lightblue",
        font_size=12,
        edge_color="gray",
    )
    # nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)

    # Save to a file and show the graph
    plt.savefig("tree_graph.png", format="png", dpi=300)
    plt.title("Tree-Like Graph Visualization")
    plt.show()
    
task2()