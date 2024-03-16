# https://codeforces.com/contest/1948/problem/C

import sys
from collections import deque
input = sys.stdin.readline

directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(input().strip()) for _ in range(2)]
    
    visited = [[[False] * n for _ in range(2)] for _ in range(2)]
    stack = deque([(0, 0, 0)])
    visited[0][0][0] = True
    
    answer = False
    while stack:
        s, r, c = stack.pop()
        if r == 1 and c == n - 1:
            answer = True
            break
        
        if s == 0:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 2 and 0 <= nc < n and not visited[1][nr][nc]:
                    stack.append((1, nr, nc))
                    visited[1][nr][nc] = True
        else:
            if arr[r][c] == ">" and c < n - 1 and not visited[0][r][c + 1]:
                stack.append((0, r, c + 1))
                visited[0][r][c + 1] = True
            elif arr[r][c] == "<" and c > 0 and not visited[0][r][c - 1]:
                stack.append((0, r, c - 1))
                visited[0][r][c - 1] = True
    print("YES" if answer else "NO")