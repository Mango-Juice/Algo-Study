# https://www.acmicpc.net/problem/1260

from collections import deque
import sys
input=sys.stdin.readline

def dfs(idx):
    target = 0
    dfs_visited.append(idx)
    while connection[idx]:
        target = connection[idx].popleft()
        if not target in dfs_visited:
            dfs(target)
            #break
    if not connection[idx]:
        return

def bfs(num):
    bfs_visited.append(num)
    to_go = deque([num])
    while True:
        idx = to_go.popleft()
        while connection_bfs[idx]:
            target = connection_bfs[idx].popleft()
            if not target in bfs_visited:
                to_go.append(target)
                bfs_visited.append(target)
        if not to_go:
            break

n, m, v = tuple(map(int, input().rstrip().split()))
connection = {i+1:deque() for i in range(n)}
connection_bfs = {}
dfs_visited = deque()
bfs_visited = deque()

for i in range(m):
    a, b = tuple(map(int, input().rstrip().split()))
    connection[a].append(b)
    connection[b].append(a)

for i in connection.keys():
    connection[i] = deque(sorted(connection[i]))
    connection_bfs[i] = deque(sorted(connection[i]))

dfs(v)
print(' '.join(map(str, dfs_visited)))
bfs(v)
print(' '.join(map(str, bfs_visited)))
