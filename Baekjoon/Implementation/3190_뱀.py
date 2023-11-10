from collections import deque
import sys
input = sys.stdin.readline

# 상수
BLANK, APPLE, SNAKE = range(3)
UP, RIGHT, DOWN, LEFT = range(4)
CW, CCW = 1, -1
DIRECTIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))

# 입력
N = int(input())
K = int(input())
arr = [[BLANK for _ in range(N + 2)] for _ in range(N + 2)]

for _ in range(K):
    r, c = map(int, input().split())
    arr[r][c] = APPLE
L = int(input())

commands = deque()
for _ in range(L):
    x, c = input().rstrip().split()
    commands.append((int(x), CW if c == 'D' else CCW))

# 벽 세우기
arr[1][1] = SNAKE
for i in range(N + 2):
    arr[0][i] = arr[i][0] = arr[N + 1][i] = arr[i][N + 1] = SNAKE

# 구현
count = 0
direction = RIGHT
snakes = deque([(1, 1)])
while True:
    count += 1

    # 1. 머리 옮기기
    dr, dc = DIRECTIONS[direction]
    hr, hc = snakes[0][0] + dr, snakes[0][1] + dc
    target = arr[hr][hc]

    if target == SNAKE:
        break
    snakes.appendleft((hr, hc))
    arr[hr][hc] = SNAKE

    # 2. 꼬리 줄이기
    if target == BLANK:
        tr, tc = snakes.pop()
        arr[tr][tc] = BLANK
    
    # 3. 방향 전환
    if commands and commands[0][0] == count:
        x, command = commands.popleft()
        direction = (direction + command + 4) % 4
    
print(count)