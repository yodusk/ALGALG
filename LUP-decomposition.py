import numpy as np


def qud_matr(matr, k=0):
    rows = matr.shape[0]
    cols = matr.shape[1]
    if k == 0:
        if rows > cols:
            cur = rows
        else:
            cur = cols
    else:
        cur = k
    while not np.log2(cur).is_integer():
        cur += 1
    new_matr = np.zeros((cur, cur))
    new_matr[:rows, :cols] = matr
    return new_matr


def strassen(first_matrix, second_matrix):
    mod = 2
    if (first_matrix.shape[0] == 1 and first_matrix.shape[1] == 1) or (
            second_matrix.shape[0] == 1 and second_matrix.shape[1] == 1):
        return first_matrix * second_matrix % mod
    rows = first_matrix.shape[0]
    cols = second_matrix.shape[1]
    r = max(first_matrix.shape[0], first_matrix.shape[1], second_matrix.shape[0], second_matrix.shape[1])
    first_matrix = qud_matr(first_matrix, r)
    second_matrix = qud_matr(second_matrix, r)
    length = first_matrix.shape[0] // 2
    cur = length * 2
    a11 = first_matrix[0:length, 0:length]
    a12 = first_matrix[0:length, length:]
    a21 = first_matrix[length:, 0:length]
    a22 = first_matrix[length:, length:]
    b11 = second_matrix[0:length, 0:length]
    b12 = second_matrix[0:length, length:]
    b21 = second_matrix[length:, 0:length]
    b22 = second_matrix[length:, length:]
    p1 = strassen((a11 + a22) % mod, (b11 + b22) % mod) % mod
    p2 = strassen((a21 + a22) % mod, b11 % mod) % mod
    p3 = strassen(a11 % mod, (b12 - b22) % mod) % mod
    p4 = strassen(a22 % mod, (b21 - b11) % mod) % mod
    p5 = strassen((a11 + a12) % mod, b22 % mod) % mod
    p6 = strassen((a21 - a11) % mod, (b11 + b12) % mod) % mod
    p7 = strassen((a12 - a22) % mod, (b21 + b22) % mod) % mod
    c11 = p1 + p4 - p5 + p7
    c12 = p3 + p5
    c21 = p2 + p4
    c22 = p1 - p2 + p3 + p6
    output_matrix = np.zeros((cur, cur))
    output_matrix[:length, :length] = c11 % mod
    output_matrix[:length, length:] = c12 % mod
    output_matrix[length:, :length] = c21 % mod
    output_matrix[length:, length:] = c22 % mod
    return output_matrix[:rows, :cols] % 2


def inv(init_matr):
    mod = 2
    length = init_matr.shape[0]
    matrix_inv = np.zeros((length, length))
    if length == 1:
        return np.array([[1]])
    else:
        div = length // 2
        a11 = init_matr[:div, :div]
        a12 = init_matr[:div, div:]
        a21 = init_matr[div:, :div]
        a22 = init_matr[div:, div:]
        a11_inv = inv(a11) % 2
        dil = (a22 % 2 - strassen(strassen(a21, a11_inv), a12) % 2) % 2
        dil_inv = inv(dil) % 2
        matrix_inv[0:div, 0:div] = (a11_inv % 2 + strassen(
            strassen(strassen(strassen(a11_inv, a12) % 2, dil_inv) % 2, a21) % 2, a11_inv) % 2) % 2
        matrix_inv[0:div, div:] = strassen(strassen(-1 * a11_inv, a12) % 2, dil_inv) % 2
        matrix_inv[div:, 0:div] = strassen(strassen(-1 * dil_inv, a21) % 2, a11_inv) % 2
        matrix_inv[div:, div:] = dil_inv
    return matrix_inv % mod


def lup_decomposition(initial_matrix):
    m = initial_matrix.shape[0]
    p = initial_matrix.shape[1]
    if m == 1:
        lower = np.array([[1]])
        permut = np.eye(p, p)
        for i in range(p):
            if initial_matrix[0][i] != 0:
                permut[:, [i, 0]] = permut[:, [0, i]]
                break
        upper = strassen(initial_matrix, permut)
        return lower, upper, permut
    else:
        mid = m // 2
        b_matr = initial_matrix[:mid, :]
        c_matr = initial_matrix[mid:, :]
        lower1, upper1, permut1 = lup_decomposition(b_matr)
        permut1_inverse = permut1.T
        d = strassen(c_matr, permut1_inverse) % 2
        e = upper1[:, :mid]
        f = d[:, :mid]
        if e[0][0] != 0:
            e_inverse = inv(e)
            g = d - strassen(strassen(f, e_inverse), upper1)
        else:
            e_inverse = e
            g = d
        mid2 = p - mid
        g1 = g[::, -mid2:]
        lower2, upper2, permut2 = lup_decomposition(g1)
        permut3 = np.eye(p, p)
        permut3[:mid, mid:] = 0
        permut3[mid:, :mid] = 0
        permut3[mid:, mid:] = permut2 % 2
        permut3_inverse = permut3.T
        h_matr = strassen(upper1, permut3_inverse) % 2
        lower = np.zeros((m, m))
        lower[:mid, :mid] = lower1
        lower[mid:, :mid] = strassen(f, e_inverse) % 2
        lower[mid:, mid:] = lower2
        upper = np.zeros((m, p))
        upper[:mid, :] = h_matr
        upper[mid:, mid:] = upper2
        permut = strassen(permut3, permut1)
        return lower, upper, permut


matrix = [[int(i) for i in input().split()]]
n = len(matrix[0]) - 1
for _ in range(n):
    matrix.append([int(i) for i in input().split()])
matrix = np.array(matrix)

Low, Up, Perm = lup_decomposition(matrix)
Low = Low.astype('int')
Up = Up.astype('int')
Perm = Perm.astype('int')
for i in Low:
    print(*i)
for i in Up:
    print(*i)
for i in Perm:
    print(*i)
