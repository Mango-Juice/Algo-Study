# https://www.acmicpc.net/problem/16678

import sys

input = sys.stdin.readline

modok = 1
answer = 0
n = int(input())
arr = sorted([int(input()) for _ in range(n)])

for i in range(n):
    if arr[i] >= modok:
        answer += arr[i] - modok
        modok += 1

print(answer)
