import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
oud = [0] * (n + 1)
ind = [0] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    oud[b] += 1
    ind[a] += 1

status = deque([n])
dp = [0] * (n + 1)
dp[n] = 1

while status:
    now_node = status.pop()
    
    for next_node, next_value in graph[now_node]:
        dp[next_node] += dp[now_node] * next_value
        oud[next_node] -= 1
        if oud[next_node] == 0:
            status.append(next_node)

for i, v in enumerate(dp):
    if i > 0 and ind[i] == 0:
        print(i, v)