import numpy as np


def strassen(first_matrix, second_matrix):
    if len(first_matrix) == 1:
        return (first_matrix * second_matrix) % 9
    first_len = len(first_matrix[0]) // 2
    second_len = len(second_matrix[0]) // 2
    a11 = first_matrix[0:first_len, 0:first_len]
    a12 = first_matrix[0:first_len, first_len:]
    a21 = first_matrix[first_len:, 0:first_len]
    a22 = first_matrix[first_len:, first_len:]
    b11 = second_matrix[0:second_len, 0:second_len]
    b12 = second_matrix[0:second_len, second_len:]
    b21 = second_matrix[second_len:, 0:second_len]
    b22 = second_matrix[second_len:, second_len:]
    p1 = strassen((a11 + a22) % 9, (b11 + b22) % 9) % 9
    p2 = strassen((a21 + a22) % 9, b11 % 9) % 9
    p3 = strassen(a11 % 9, (b12 - b22) % 9) % 9
    p4 = strassen(a22 % 9, (b21 - b11) % 9) % 9
    p5 = strassen((a11 + a12) % 9, b22 % 9) % 9
    p6 = strassen((a21 - a11) % 9, (b11 + b12) % 9) % 9
    p7 = strassen((a12 - a22) % 9, (b21 + b22) % 9) % 9
    c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5
    c21 = p2 + p4
    c22 = p1 - p2 + p3 + p6
    output_matrix = np.zeros((len(first_matrix[0]), len(first_matrix)))
    output_matrix[0:first_len, 0:first_len] = c11 % 9
    output_matrix[0:first_len, first_len:] = c12 % 9
    output_matrix[first_len:, 0:first_len] = c21 % 9
    output_matrix[first_len:, first_len:] = c22 % 9
    return output_matrix


matrix = [[int(i) for i in input().split()]]
n = len(matrix[0])
power = n - 1
rows = len(matrix[0]) - 1
while not np.log2(n).is_integer():
    n += 1

lng = n - len(matrix[0])
for _ in range(lng):
    matrix[0].append(0)
counter = 0
while counter < rows:
    matrix.append([int(i) for i in input().split()])
    for _ in range(lng):
        matrix[counter + 1].append(0)
    counter += 1
for _ in range(lng):
    matrix.append([0 for i in range(n)])

matrix = np.array(matrix)

count = 1
initial_matrix = matrix
while count <= power:
    if count * 2 < power:
        matrix = strassen(matrix, matrix)
        count *= 2
    else:
        matrix = strassen(matrix, initial_matrix)
        count += 1
if power != 0:
    output = matrix[0:-lng, 0:-lng].astype(int)
else:
    output = matrix
for i in output:
    print(*i)
