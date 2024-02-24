import sys
input = sys.stdin.readline


def find(x):
    if dset[x] == x:
        return x
    dset[x] = find(dset[x])
    return dset[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x!= y:
        dset[max(x, y)] = min(x, y)


n, p = map(int, input().split())
costs = [0] + [int(input()) for _ in range(n)]
nodes = []

for _ in range(p):
    f, t, w = map(int, input().split())
    nodes.append((2 * w + costs[f] + costs[t], f, t))

nodes.sort()
dset = [i for i in range(n + 1)]
count = cost = 0

for w, f, t in nodes:
    x = find(f)
    y = find(t)
    
    if x != y:
        union(x, y)
        count += 1
        cost += w
    
    if count == n - 1:
        break

print(cost + min(costs[1:]))