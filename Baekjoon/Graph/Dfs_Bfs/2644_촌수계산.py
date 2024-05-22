import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n + 1)]
chon = [-1] * (n + 1)

for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

chon[a] = 0
q = deque([a])

while q:
    now = q.popleft()
    for next in arr[now]:
        if chon[next] < 0:
            chon[next] = chon[now] + 1
            if next == b:
                print(chon[b])
                exit()
            q.append(next)

print(chon[b])