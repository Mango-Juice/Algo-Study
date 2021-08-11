# https://www.acmicpc.net/problem/16946

import sys
from collections import deque
input = sys.stdin.readline

DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))


def get_result(a: int, b: int) -> int:
    result = 1
    used = []
    
    for dx, dy in DIRECTIONS:
        newx, newy = a + dx, b + dy
        
        if newx >= 0 and newx < n and newy >= 0 and newy < m and cnt_map[newx][newy] > 0 and not cnt_map[newx][newy] in used:
            used.append(cnt_map[newx][newy])
            result += groups[cnt_map[newx][newy]]

    return result


def set_map(a: int, b: int, c: int) -> None:
    visited[a][b] = True
    q = deque([(a, b)])
    groups[c] = 1
    cnt_map[a][b] = c

    while q:
        x, y = q.popleft()

        for dx, dy in DIRECTIONS:
            newx, newy = x + dx, y + dy
            
            if newx >= 0 and newx < n and newy >= 0 and newy < m and arr[newx][newy] == 0 and not visited[newx][newy]:
                visited[newx][newy] = True
                q.append((newx, newy))
                groups[c] += 1
                cnt_map[newx][newy] = c


n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]
cnt_map = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
groups = {}
group_count = 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 0 and not visited[i][j]:
            set_map(i, j, group_count)
            group_count += 1

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            arr[i][j] = get_result(i, j) % 10

for i in range(n):
    print(*arr[i], sep = '')
