# https://www.acmicpc.net/problem/10830

import sys
sys.setrecursionlimit(500000)
input = sys.stdin.readline
MOD = 1000


def multiply(ma: list[list[int]], mb: list[list[int]]) -> list[list[int]]:
    global N
    result = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] = (result[i][j] + ma[i][k] * mb[k][j]) % MOD

    return result


def pow(arr: list[list[int]], n: int) -> list[list[int]]:
    if n == 1:
        return arr

    new_arr = pow(arr, n // 2)
    new_arr = multiply(new_arr, new_arr)

    if n & 1:
        new_arr = multiply(new_arr, arr)

    return new_arr


N, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(*map(lambda x: ' '.join(map(lambda y: str(y % MOD), x)), pow(arr, B)), sep='\n')
