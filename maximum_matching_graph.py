import numpy as np

n = int(input())
edges = []
cur = 1
for _ in range(n):
    left_node, right_node = input().split()
    left_node = int(left_node)
    right_node = int(right_node)
    if cur < left_node:
        cur = left_node
    if cur < right_node:
        cur = right_node
    edges.append((left_node, right_node))
cur += 1


def inverse(num, mod):
    inv = 1
    x = 0
    y = 0
    y2 = 1
    while mod:
        q = num // mod
        num, mod = mod, num % mod
        inv, x = x, inv - x * q
        y, y2 = y2, y - y2 * q
    return inv


def build_matrix(num, lst):
    matrix = np.zeros((num, num), dtype=np.int64)
    for i, j in lst:
        matrix[i, j] = np.random.randint(1, 8051)
    return matrix


def gauss(num, lst):
    matrix = build_matrix(num, lst)
    for k in range(cur):
        if matrix[k, k] == 0:
            for i in range(k + 1, cur):
                if matrix[i, k] != 0:
                    matrix[[k, i]] = matrix[[i, k]]
                    break
        matrix[k] = (matrix[k] * inverse(matrix[k, k], 8051) % 8051)
        for i in range(k + 1, cur):
            coef = matrix[i, k] * inverse(matrix[k, k], 8051)
            for j in range(cur):
                matrix[i, j] = (matrix[i, j] - matrix[k, j] * coef % 8051) % 8051
    for i in range(cur):
        if matrix[i, i] == 0:
            return False
    return True


ans = "yes"
for _ in range(4):
    if not gauss(cur, edges):
        ans = 'no'

print(ans)