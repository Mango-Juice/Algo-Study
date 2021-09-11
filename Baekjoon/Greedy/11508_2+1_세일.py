# https://www.acmicpc.net/problem/11508

import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([int(input()) for _ in range(n)], reverse=True)
idx = answer = 0

while idx < n - 2:
    answer += arr[idx] + arr[idx + 1]
    idx += 3

while idx < n:
    answer += arr[idx]
    idx += 1

print(answer)
