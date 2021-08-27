# https://www.acmicpc.net/problem/1034

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
k = int(input())
answer = 0

for i in range(n):
    zero_count = m - sum(arr[i])
    result = 0

    if zero_count <= k and zero_count % 2 == k % 2:
        for j in range(n):
            if arr[i] == arr[j]:
                result += 1

    answer = max(answer, result)

print(answer)
