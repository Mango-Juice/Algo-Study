# https://www.acmicpc.net/problem/2623
# 위상 정렬

from collections import deque
from sys import stdin

N, M = map(int, stdin.readline().split())
indegree = [0] * (N + 1)
result = []
graph = [[] for i in range(N + 1)]
queue = deque()

for _ in range(M):
    inp = list(map(int, stdin.readline().split()))
    for i in range(1, inp[0]):
        graph[inp[i]].append(inp[i + 1])
        indegree[inp[i + 1]] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    target = queue.popleft()
    result.append(target)

    for i in graph[target]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)


if len(result) < N:
    print(0)
else:
    for i in result:
        print(i)
