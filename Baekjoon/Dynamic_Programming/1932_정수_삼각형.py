# https://www.acmicpc.net/problem/1932

import sys

input = sys.stdin.readline

n = int(input())

arr = []

for i in range(n):
    tmp = []
    
    for j, value in enumerate(map(int, input().split())):
        target1 = target2 = value
        
        if j > 0:
            target1 += arr[i - 1][j - 1]
        if j < i:
            target2 += arr[i - 1][j]

        tmp.append(max(target1, target2))

    arr.append(tmp)

print(max(arr[n - 1]))
