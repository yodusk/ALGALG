import numpy as np


def create_inputs(num, dict1, dict2):
    gen_bin = []
    for number in range(0, 2 ** num):
        gen_bin.append(bin(number)[2:].zfill(num))

    to_truth = []
    for bit_num in gen_bin:
        out_lst = []
        for bit in bit_num:
            out_lst.append(int(bit))
        to_truth.append(out_lst)

    arr = np.array(to_truth)
    arr = arr.transpose().tolist()
    for index in enumerate(arr):
        toad = arr[index[0]]
        toad = tuple(toad)
        dict1[index[0]] = [0, 0, "INPUT", toad]
        dict2.add(toad)


def create_nots(dict1, dict2, dict3):
    global ngates
    lst1 = list(dict1.keys())
    for bit1 in lst1:  # строим ноты
        bittr = []
        for bit2 in dict1[bit1][3]:
            if bit2 == 1:
                bittr.append(0)
            else:
                bittr.append(1)
        toad = tuple(bittr)
        dict3[ngates] = [bit1, 0, "NOT", toad]
        dict2.add(toad)
        ngates += 1


def create_conjunctions(dict1, dict2, dict3, dict4):
    global ngates
    lst1 = list(dict1.keys())
    lst2 = list(dict2.keys())
    for key1 in lst1:
        tru1 = dict1[key1][3]
        for key2 in lst2:
            tru2 = dict2[key2][3]
            new_tru = []
            for k in enumerate(tru1):
                if tru1[k[0]] == 1 and tru2[k[0]] == 1:
                    new_tru.append(1)
                else:
                    new_tru.append(0)
            new_tru = tuple(new_tru)
            if new_tru not in dict3:
                dict4[ngates] = [key1, key2, "AND", new_tru]
                dict3.add(new_tru)
                ngates += 1


def create_disjunctions(dict1, dict2, dict3, dict4):
    global ngates
    lst1 = list(dict1.keys())
    lst2 = list(dict2.keys())
    for bit1 in lst1:
        tru1 = dict1[bit1][3]
        for bit2 in lst2:
            tru2 = dict2[bit2][3]
            new_tru = []
            for k in enumerate(tru1):
                if tru1[k[0]] == 0 and tru2[k[0]] == 0:
                    new_tru.append(0)
                else:
                    new_tru.append(1)
            new_tru = tuple(new_tru)
            if new_tru not in dict3:
                dict4[ngates] = [bit1, bit2, "OR", new_tru]
                dict3.add(new_tru)
                ngates += 1


n = int(input())
scheme = {}
truth_tables = set()
ngates = n

create_inputs(n, scheme, truth_tables)
create_nots(scheme, truth_tables, scheme)
for _ in range(n):
    create_conjunctions(scheme, scheme, truth_tables, scheme)
for _ in range(n):
    create_disjunctions(scheme, scheme, truth_tables, scheme)

for element in scheme:
    if scheme[element][2] == "INPUT":
        continue
    elif scheme[element][2] == "NOT":
        print(f"GATE {element} {scheme[element][2]} {scheme[element][0]}")
    else:
        print(f"GATE {element} {scheme[element][2]} {scheme[element][0]} {scheme[element][1]}")

count = 0
for output in scheme:
    print(f"OUTPUT {count} {output}")
    count += 1
