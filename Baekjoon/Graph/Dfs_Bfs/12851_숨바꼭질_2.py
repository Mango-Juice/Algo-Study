import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

visited = [float('inf')] * (2 * max(n, k) + 1)
answer = count = -1
q = deque([(n, 0)])
visited[n] = 0

while q:
    now, time = q.popleft()
    
    if now == k:
        if answer == -1:
            answer = time
            count = 1
        elif answer == time:
            count += 1
        else:
            break
        continue
    
    if now + 1 < len(visited) and visited[now + 1] > time:
        q.append((now + 1, time + 1))
        visited[now + 1] = time + 1
    if now > 0 and visited[now - 1] > time:
        q.append((now - 1, time + 1))
        visited[now - 1] = time + 1
    if now * 2 < len(visited) and visited[now * 2] > time:
        q.append((now * 2, time + 1))
        visited[now * 2] = time + 1


print(answer)
print(count)