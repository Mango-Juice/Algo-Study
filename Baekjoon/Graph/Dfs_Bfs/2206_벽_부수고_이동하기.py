# https://www.acmicpc.net/problem/2206

from collections import deque
import sys
input = sys.stdin.readline

LIMIT = 1
DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
n, m = map(int, input().split())
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(LIMIT + 1)]
arr = []
q = deque([(0, 0, 0, 1)])
answer = -1

for _ in range(n):
    arr.append(list(map(int, input().rstrip())))

while q:
    r, c, b, count = q.popleft()

    if r == n - 1 and c == m - 1:
        answer = count
        break
    
    if visited[b][r][c]: continue
    visited[b][r][c] = True
    
    for dr, dc in DIRECTIONS:
        newr, newc = r + dr, c + dc

        if newr >= 0 and newr < n and newc >= 0 and newc < m:
            if arr[newr][newc] == 0: q.append((newr, newc, b, count + 1))
            elif b < LIMIT: q.append((newr, newc, b + 1, count + 1))

print(answer)
