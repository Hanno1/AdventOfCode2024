import helperfunction as hc

def compare_files(file1, file2):
    data1 = hc.read_file_line(file1)
    data2 = hc.read_file_line(file2)
    print(len(data1), len(data2))
    not_in_data1 = []
    not_in_data2 = []
    for i in range(len(data1)):
        if data1[i] not in data2:
            not_in_data1.append(data1[i])
    for i in range(len(data2)):
        if data2[i] not in data1:
            not_in_data2.append(data2[i])
    print(not_in_data1)
    print(not_in_data2)
    
compare_files("282", "285")