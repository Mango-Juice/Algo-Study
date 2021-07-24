#https://www.acmicpc.net/problem/2579

import sys

input = sys.stdin.readline

n = int(input())
dp1 = [0] * n
dp2 = [0] * n

for i in range(n):
    inp = int(input())
    
    if i < 2:
        dp1[i] = inp
    else:
        dp1[i] = max(dp2[i - 2], dp1[i - 2]) + inp

    if i > 0:
        dp2[i] = dp1[i - 1] + inp

print(max(dp1[n - 1], dp2[n - 1]))
