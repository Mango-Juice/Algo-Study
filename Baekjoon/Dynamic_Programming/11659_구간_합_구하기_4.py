# https://www.acmicpc.net/problem/11659

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0]

for i in map(int, input().split()):
    arr.append(arr[-1] + i)

for _ in range(m):
    i, j = map(int, input().split())
    print(arr[j] - arr[i - 1])
