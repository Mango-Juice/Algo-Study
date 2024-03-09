import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [float('inf')] * (2 * max(n, k) + 1)
track = [-1] * (2 * max(n, k) + 1)
answer = count = -1
q = deque([(n, 0)])
visited[n] = 0

while q:
    now, time = q.popleft()
    
    if now == k:
        answer = time
        break
    
    if now + 1 < len(visited) and visited[now + 1] > time + 1:
        q.append((now + 1, time + 1))
        visited[now + 1] = time + 1
        track[now + 1] = now
    if now > 0 and visited[now - 1] > time + 1:
        q.append((now - 1, time + 1))
        visited[now - 1] = time + 1
        track[now - 1] = now
    if now * 2 < len(visited) and visited[now * 2] > time + 1:
        q.append((now * 2, time + 1))
        visited[now * 2] = time + 1
        track[now * 2] = now

arr = [k]
now = k

while now != n:
    next = track[now]
    arr.append(next)
    now = next

print(answer)
print(*arr[::-1])