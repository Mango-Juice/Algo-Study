# https://www.acmicpc.net/problem/1911

import sys, math
input = sys.stdin.readline

n, l = map(int, input().split())
arr = sorted([tuple(map(int, input().split())) for _ in range(n)])
gol_left = -1
answer = 0

for le, right in arr:
    left = max(le, gol_left)
    gol_need = math.ceil((right - left) / l)
    answer += gol_need
    gol_left = left + gol_need * l

print(answer)
