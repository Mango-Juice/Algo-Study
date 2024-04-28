import sys
from collections import deque
input = sys.stdin.readline
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find(x):
    if x != disjoint[x]:
        disjoint[x] = find(disjoint[x])
    return disjoint[x]


def union(x, y):
    x = find(x)
    y = find(y)
    disjoint[max(x, y)] = min(x, y)
    return x != y



n, m = map(int, input().split())
arr = []
k = 1
targets = {}

for i in range(n):
    inp = list(input().rstrip())
    for j, s in enumerate(inp):
        if s == "S":
            inp[j] = 0
            targets[0] = (i, j)
        elif s == "K":
            inp[j] = k
            targets[k] = (i, j)
            k += 1
        
    arr.append(list(inp))

edges = set()
for i in range(m + 1):
    distances = [[None] * n for _ in range(n)]
    q = deque([targets[i]])
    distances[targets[i][0]][targets[i][1]] = 0
    
    while q:
        r, c = q.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if arr[nr][nc] == "1" or distances[nr][nc] is not None: continue
            distances[nr][nc] = distances[r][c] + 1
            q.append((nr, nc))
            if type(arr[nr][nc]) == int:
                edges.add((distances[nr][nc], min(i, arr[nr][nc]), max(i, arr[nr][nc])))

edges = sorted(edges)
answer = 0
disjoint = [i for i in range(m + 1)]
for cost, origin, target in edges:
    if union(origin, target):
        answer += cost

target = find(0)
for i in range(m + 1):
    if find(i) != target:
        answer = -1
        break

print(answer)