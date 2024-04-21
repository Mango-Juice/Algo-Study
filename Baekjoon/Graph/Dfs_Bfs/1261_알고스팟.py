import sys
from collections import deque
input = sys.stdin.readline

directions = ((-1, 0), (1, 0), (0, -1), (0, 1))
m, n = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

answer = [[float('inf')] * m for _ in range(n)]
answer[0][0] = 0

q = deque([(0, 0)])
while q:
    r, c = q.popleft()
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
        if arr[nr][nc] == 0 and answer[nr][nc] > answer[r][c]:
            answer[nr][nc] = answer[r][c]
            q.appendleft((nr, nc))
        elif answer[nr][nc] > answer[r][c] + 1:
            answer[nr][nc] = answer[r][c] + 1
            q.append((nr, nc))
        if nr == n - 1 and nc == m - 1:
            print(answer[n - 1][m - 1])
            exit()

print(0)