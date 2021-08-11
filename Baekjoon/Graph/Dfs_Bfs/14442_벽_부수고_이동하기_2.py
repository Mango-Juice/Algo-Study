# https://www.acmicpc.net/problem/14442

import sys
from collections import deque
input = sys.stdin.readline

DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))

def bfs():
    q = deque([(0, 0, 0)])

    while q:
        x, y, c = q.popleft()
        
        if x == n - 1 and y == m - 1:
            return visited[x][y][c]

        dist = visited[x][y][c] + 1

        for dx, dy in DIRECTIONS:
            tx, ty = dx + x, dy + y
            
            if 0 <= tx < n and 0 <= ty < m:
                if not arr[tx][ty] and not visited[tx][ty][c]:
                    visited[tx][ty][c] = dist
                    q.append((tx, ty, c))

                elif c < k and not visited[tx][ty][c + 1]: 
                    visited[tx][ty][c + 1] = dist
                    q.append((tx, ty, c + 1)) 
    return -1

n, m, k = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
visited = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
visited[0][0] = [1] * (k + 1)

print(bfs())
