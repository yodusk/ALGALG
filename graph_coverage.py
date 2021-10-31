num_nodes = int(input())
x = [0 for i in range(num_nodes)]
w = [0 for i in range(num_nodes)]
for i in range(num_nodes):
    w[i] = int(input())

num_edges = int(input())
edges = []
y = [0 for i in range(num_edges)]
for _ in range(num_edges):
    e1, e2 = map(int, input().split())
    edges.append((e1, e2))

k = 0
for e in edges:
    i = e[0]
    j = e[1]
    y[k] = min(w[i] - x[i], w[j] - x[j])
    x[i] += y[k]
    x[j] += y[k]
    k += 1

res = []
for i in range(num_nodes):
    if w[i] == x[i]:
        res.append(i)

print(*res)
