import numpy as np


def build_hadamar(n):
    matrix = np.zeros((n, n)).astype('int')
    p = n - 1
    addit = [0 for i in range(2 * p)]
    for index1 in range(p):
        addit[index1] = -1
    for index2 in range(1, (p - 1) // 2 + 1):
        addit[index2 * index2 % p] = 1
    for col_index in range(p, 2 * p):
        addit[col_index] = addit[col_index - p]
    for row_index in range(n):
        matrix[0][row_index] = 1
    for b in range(1, n):
        matrix[b][0] = 1
    for index1 in range(1, n):
        for index2 in range(1, n):
            matrix[index1][index2] = addit[index2 - index1 + p]
    return matrix


j = int(input())
first_out = build_hadamar(j)
second_out = np.copy(first_out)
first_out[first_out == -1] = 0
second_out[second_out == 1] = 0
second_out[second_out == -1] = 1
for i in first_out:
    for k in i:
        print(k, end='')
    print()
for i in second_out:
    for k in i:
        print(k, end='')
    print()
