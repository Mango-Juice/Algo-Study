# https://www.acmicpc.net/problem/1002

import sys, math

t = int(sys.stdin.readline())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    rs = sorted([distance, r1, r2], reverse = True)

    if r1 == r2 and distance == 0: # 일치
        print(-1)
    elif distance == r1 + r2 or max(r1, r2) == min(r1, r2) + distance: # 교점 1개
        print(1)
    elif rs[0] > rs[1] + rs[2]: # 교점 0개
        print(0)
    else: # 교점 2개
        print(2)
