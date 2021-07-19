# https://www.acmicpc.net/problem/1987

import sys
from collections import deque

def bfs(x: int, y: int) -> int:
    answer = 1
    queue = deque([(x, y, arr[x][y])])

    while queue:
        qx, qy, alphas = queue.pop()

        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if 0 <= nx < r and 0 <= ny < c and not arr[nx][ny] in alphas:
                queue.append((nx, ny, alphas + arr[nx][ny]))
                answer = max(answer, len(alphas) + 1)

    return answer
        

r, c = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
