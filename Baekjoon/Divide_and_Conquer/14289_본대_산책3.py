# https://www.acmicpc.net/problem/14289

from sys import stdin
input = stdin.readline

MOD = 1000000007

def mul(a, b):
    result = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n): tmp += a[i][k] * b[k][j]
            result[i][j] = tmp % MOD

    return result

n, m = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 1
    arr[b - 1][a - 1] = 1

d = int(input())

answer = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n): answer[i][i] = 1

while d > 0:
    if d % 2 > 0:
        answer = mul(answer, arr)
        d -= 1
    arr = mul(arr, arr)
    d //= 2

print(answer[0][0])
