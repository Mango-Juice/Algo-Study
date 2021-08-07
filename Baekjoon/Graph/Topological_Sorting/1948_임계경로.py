# https://www.acmicpc.net/problem/1948

# ===== 라이브러리 ===== #

from collections import deque
import sys

input = sys.stdin.readline

# ===== 입력 ===== #

n = int(input())
m = int(input())

tree = [[] for _ in range(n + 1)]
reverse_tree = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    indegree[b] += 1
    tree[a].append((b, c))
    reverse_tree[b].append((a, c))

start, finish = map(int, input().split())

# ===== 위상 정렬로 만나는 시간 찾기 ===== #

time = [0] * (n + 1)

q = deque([start])

while q:
    target = q.popleft()
    for destination, cost in tree[target]:
        indegree[destination] -= 1
        time[destination] = max(time[destination], cost + time[target])
        if indegree[destination] == 0:
            q.append(destination)

# ===== 거꾸로 돌아가면서 쉬지 않는 도로인지 확인 ===== #

visited = [False] * (n + 1)
answer = 0

q.append(finish)

while q:
    target = q.popleft()
    for destination, cost in reverse_tree[target]:
        # destination에서 target으로 가는 길 중 가장 긴 도로인지 확인
        if time[target] - time[destination] == cost:
            answer += 1
            if not visited[destination]:
                q.append(destination)
                visited[destination] = True

# ===== 출력 ===== #

print(time[n])
print(answer)
