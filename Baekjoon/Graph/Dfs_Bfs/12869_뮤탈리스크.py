import sys
from collections import deque
input = sys.stdin.readline

dv = ((9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 3, 9), (1, 9, 3))

n = int(input())
now = tuple(sorted(map(int, input().split())) + [0] * (3 - n))
visited = [[[False] * 61 for _ in range(61)] for _ in range(61)]

q = deque([(now, 0)])
visited[now[0]][now[1]][now[2]] = True
while q:
    (a, b, c), count = q.popleft()
    
    for da, db, dc in dv:
        na, nb, nc = sorted([max(0, a - da), max(0, b - db), max(0, c - dc)])
        if na == nb == nc == 0:
            print(count + 1)
            exit()
        if not visited[na][nb][nc]:
            q.append(((na, nb, nc), count + 1))
            visited[na][nb][nc] = True