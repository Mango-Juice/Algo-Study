# https://www.acmicpc.net/problem/2178

from collections import deque
import sys

input = sys.stdin.readline
DIRECTIONS = ((0, 1), (0, -1), (1, 0), (-1, 0))

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
answer = -1

queue = deque([(0, 0, 1)])
arr[0][0] = '0'

while queue:
    tx, ty, cnt = queue.popleft()

    for dx, dy in DIRECTIONS:
        nx, ny = tx + dx, ty + dy

        if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == '1':
            queue.append((nx, ny, cnt + 1))
            arr[nx][ny] = '0'

            if nx == N - 1 and ny == M - 1:
                answer = cnt + 1
                break

print(answer)
