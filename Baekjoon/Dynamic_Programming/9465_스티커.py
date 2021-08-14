# https://www.acmicpc.net/problem/9465

import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [[0] + list(map(int, input().split())) for _ in range(2)]

    for i in range(2, n + 1):
        arr[0][i] += max(arr[1][i - 1], arr[1][i - 2])
        arr[1][i] += max(arr[0][i - 1], arr[0][i - 2])

    print(max(arr[0][n], arr[1][n]))
