# Sparse Table
import sys
import math
input = sys.stdin.readline

def make_parents(target):
    global parents
    for child, weight in graph[target]:
        if parents[child][0] == 0:
            parents[child] = [target, weight]
            make_parents(child)


def query(target, energy):
    for i in range(logn - 1, -1, -1):
        parent, weight = sparse[i][target]
        if parent > 0 and energy >= weight:
            target = parent
            energy -= weight
        if energy <= 0: break
    return target


n = int(input())
ants = [0] + [int(input()) for _ in range(n)]
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    f, t, w = map(int, input().split())
    graph[f].append((t, w))
    graph[t].append((f, w))

logn = int(math.log(n, 2)) + 1
sparse = [[[0, 0] for _ in range(n + 1)] for _ in range(logn)]
parents = [[0, 0] for _ in range(n + 1)]

parents[1] = [1, 0]
make_parents(1)

for i in range(logn):
    for j in range(1, n + 1):
        if i == 0:
            sparse[i][j] = parents[j]
        else:
            next = sparse[i - 1][j]
            sparse[i][j][0] = sparse[i - 1][next[0]][0]
            sparse[i][j][1] = sparse[i - 1][next[0]][1] + sparse[i - 1][j][1]

for i in range(1, n + 1):
    print(query(i, ants[i]))