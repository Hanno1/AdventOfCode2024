import helperfunction as hc    

def read_input():
    input = hc.read_file_line("01")
    list1 = []
    list2 = []
    for entry in input:
        l1, l2 = entry.split("   ")
        list1.append(l1)
        list2.append(l2)
    return list1, list2

def task1():
    list1, list2 = read_input()
    list1.sort(reverse=True)
    list2.sort(reverse=True)
    distance = 0
    for index in range(len(list1)):
        distance += abs(int(list1[index]) - int(list2[index]))
    print(distance)
    
def task2():
    list1, list2 = read_input()
    dict2 = {}
    for entry in list2:
        if entry in dict2:
            dict2[entry] += 1
        else:
            dict2[entry] = 1
    similarity_score = 0
    for entry in list1:
        if entry in dict2:
            similarity_score += int(entry) * dict2[entry]
    print(similarity_score)
    
task2()