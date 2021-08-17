# https://www.acmicpc.net/problem/12850

MOD = 1000000007
arr = [[0, 1, 1, 0, 0, 0, 0, 0],
       [1, 0, 1, 0, 1, 0, 0, 0],
       [1, 1, 0, 1, 1, 0, 0, 0],
       [0, 0, 1, 0, 1, 1, 0, 1],
       [0, 1, 1, 1, 0, 1, 0, 0],
       [0, 0, 0, 1, 1, 0, 1, 0],
       [0, 0, 0, 0, 0, 1, 0, 1],
       [0, 0, 0, 1, 0, 0, 1, 0]]

def mul(a, b):
    result = [[0 for _ in range(8)] for _ in range(8)]
    
    for i in range(8):
        for j in range(8):
            tmp = 0
            for k in range(8): tmp += a[i][k] * b[k][j]
            result[i][j] = tmp % MOD

    return result
    
n = int(input())

answer = [[0 for _ in range(8)] for _ in range(8)]
for i in range(8): answer[i][i] = 1

while n > 0:
    if n % 2 > 0:
        answer = mul(answer, arr)
        n -= 1
    arr = mul(arr, arr)
    n //= 2

print(answer[0][0])
