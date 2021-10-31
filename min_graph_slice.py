import numpy as np

n = int(input())
cur = 1
edges = []
for _ in range(n):
    first_edge, second_edge = input().split()
    first_edge = int(first_edge)
    second_edge = int(second_edge)
    temp = max(first_edge, second_edge)
    edges.append((first_edge, second_edge))
    if temp > cur:
        cur = temp

cur += 1
laplas = np.zeros((cur, cur)).astype('int')
for edge in edges:
    laplas[edge[0]][edge[1]] = -1
    laplas[edge[1]][edge[0]] = -1

for i in range(cur):
    laplas[i][i] = len(np.where(laplas[:, i] == -1)[0])

eigenvals = np.linalg.eigh(laplas)[1][:, 1]
vector_sort = np.argsort(eigenvals)
laplas = laplas[vector_sort]
cur_plot = np.inf
answer = [np.inf]
for i in range(1, cur // 2):
    cur_clus = laplas[:i, :].copy()
    low = len(np.where(cur_clus == -1)[0])
    plot = low / (len(np.where(laplas == -1)[0]) - low)
    if plot <= cur_plot:
        new_ans = sorted(vector_sort[:i])
        old_ans = sorted(answer)
        if plot == cur_plot:
            if new_ans[0] < old_ans[0]:
                answer = vector_sort[:i]
                cur_plot = plot
        else:
            answer = vector_sort[:i]
            cur_plot = plot

for j in range(cur - 1, cur // 2, -1):
    cur_clus = laplas[j:, :].copy()
    cur_clus = np.delete(cur_clus, vector_sort[j:], 1)
    low = len(np.where(cur_clus == -1)[0])
    plot = low / (len(np.where(laplas == -1)[0]) - low)
    if plot <= cur_plot:
        new_ans = sorted(vector_sort[j:])
        old_ans = sorted(answer)
        if plot == cur_plot:
            if new_ans[0] < old_ans[0]:
                answer = vector_sort[j:]
                cur_plot = plot
        else:
            answer = vector_sort[j:]
            cur_plot = plot

print(*answer)
