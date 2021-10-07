# https://www.acmicpc.net/problem/2170

import sys
input = sys.stdin.readline

arr = sorted(tuple(map(int, input().split())) for _ in range(int(input())))
answer = 0
left = right = None

for l, r in arr:
    if left == None: left, right = l, r
    elif left != None and l <= right: right = max(r, right)
    else:
        answer += right - left
        left, right = l, r

print(answer - left + right)
