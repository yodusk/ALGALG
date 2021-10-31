import math


def create_scheme_template(n):
    scheme = []
    for _ in range(math.ceil(math.log2(n)) + 2):
        scheme.append([0 for _ in range(n)])
    return scheme


def set_func_elements(some_scheme, level=0, gate=0, step=0):
    for i in range(0, len(some_scheme[0])):
        if i + step >= len(some_scheme[0]):
            break
        some_scheme[level][i + step] = gate
        gate += 1
    if level <= len(some_scheme) - 2:
        level += 1
        step = 2 ** (level - 1)
        set_func_elements(some_scheme, level, gate, step)


def get_left_node(some_scheme, level, num_of_elem):
    step = 2 ** (level - 1)
    while some_scheme[level - 1][num_of_elem - step] == 0 and level != 0:
        level -= 1
    return some_scheme[level - 1][num_of_elem - step]


def get_upper_node(some_scheme, level, num_of_elem):
    while some_scheme[level - 1][num_of_elem] == 0 and level != 0:
        level -= 1
    return some_scheme[level - 1][num_of_elem]


def describe_gates(some_scheme):
    num_levels = len(some_scheme)
    num_elem = len(some_scheme[0])
    for i in range(1, num_levels):
        for j in range(1, num_elem):
            if some_scheme[i][j] != 0:
                print(
                    f"GATE {some_scheme[i][j]} OR {get_left_node(some_scheme, i, j)} "
                    f"{get_upper_node(some_scheme, i, j)}")


def get_first_out(some_scheme, elem_num):
    return some_scheme[0][elem_num]


def get_second_out(some_scheme, elem_num):
    level_of_search = len(some_scheme) - 1
    while some_scheme[level_of_search][elem_num] == 0 and level_of_search >= 0:
        level_of_search -= 1
    return some_scheme[level_of_search][elem_num]


def describe_outputs(some_scheme):
    output_level = len(some_scheme) - 1
    for i in range(len(some_scheme[output_level])):
        print(f"OUTPUT {get_first_out(some_scheme, i)} {get_second_out(some_scheme, i)}")


def describe_scheme(number_of_inputs):
    schema = create_scheme_template(number_of_inputs)
    set_func_elements(schema)
    describe_gates(schema)
    describe_outputs(schema)


elements = int(input())
describe_scheme(elements)
