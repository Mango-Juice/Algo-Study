# https://www.acmicpc.net/problem/2230

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for _ in range(n): arr.append(int(input()))
arr.sort()

if m == 0 or n == 1: print(0)
else:
    l, r, answer = 0, 1, float('inf')
    
    while r < n:
        cha = arr[r] - arr[l]
        if cha < m: r += 1
        else:
            answer = min(answer, cha)
            l += 1
            r = l + 1

        if answer == m: break

    print(answer)
