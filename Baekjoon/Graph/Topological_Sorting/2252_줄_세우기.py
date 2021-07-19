# https://www.acmicpc.net/problem/2252
# 위상 정렬

from collections import defaultdict, deque

n, m = map(int, input().split())
heights = defaultdict(list)
enters = defaultdict(int)
not_visited = list(range(1, n + 1))
queue = deque()
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    heights[a].append(b)
    enters[b] += 1

while not_visited:
    for i in not_visited:
        if enters[i] == 0:
            queue.append(i)

    while queue:
        target = queue.popleft()
        not_visited.remove(target)
        answer.append(target)
        for i in heights[target]:
            enters[i] -= 1

print(' '.join(map(str, answer)))
