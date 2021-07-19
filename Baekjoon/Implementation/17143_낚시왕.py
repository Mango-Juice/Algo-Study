# https://www.acmicpc.net/problem/17143

import sys

UP, DOWN, RIGHT, LEFT = range(1, 5)
ALIVE, DEAD = True, False

directions = ((), (-1, 0), (1, 0), (0, 1), (0, -1))
R, C, M = map(int, sys.stdin.readline().split())
arr = [[-1 for _ in range(C)] for _ in range(R)]
sharks = {}
answer = 0

for i in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    arr[r - 1][c - 1] = i
    
    if d == UP or d == DOWN:
        s %= (R - 1) * 2
    else:
        s %= (C - 1) * 2
        
    sharks[i] = [ALIVE, r - 1, c - 1, s, d, z]

for i in range(C): # 이동
    # 낚시
    for j in range(R):
        if arr[j][i] > -1:
            sharks[arr[j][i]][0] = DEAD
            answer += sharks[arr[j][i]][5]
            arr[j][i] = -1
            break

    # 이동
    for idx, info in sharks.items():
        if info[0] == ALIVE:
            if arr[info[1]][info[2]] == idx:
                arr[info[1]][info[2]] = -1
            to_go_r = info[1]
            to_go_c = info[2]
            speed = info[3]

            while speed > 0:
                if to_go_c == 0 and info[4] == LEFT:
                    info[4] = RIGHT
                elif to_go_c == C - 1 and info[4] == RIGHT:
                    info[4] = LEFT
                elif to_go_r == 0 and info[4] == UP:
                    info[4] = DOWN
                elif to_go_r == R - 1 and info[4] == DOWN:
                    info[4] = UP

                to_go_r += directions[info[4]][0]
                to_go_c += directions[info[4]][1]

                speed -= 1

            # 상어가 이미 있으면 둘 중 하나가 잡아먹힘
            if -1 < arr[to_go_r][to_go_c] <= idx:
                if sharks[arr[to_go_r][to_go_c]][5] > info[5]:
                    sharks[idx][0] = DEAD
                else:
                    sharks[arr[to_go_r][to_go_c]][0] = DEAD
                    arr[to_go_r][to_go_c] = idx
                    sharks[idx][2] = to_go_c
                    sharks[idx][1] = to_go_r
            else:
                arr[to_go_r][to_go_c] = idx
                sharks[idx][2] = to_go_c
                sharks[idx][1] = to_go_r

print(answer)
