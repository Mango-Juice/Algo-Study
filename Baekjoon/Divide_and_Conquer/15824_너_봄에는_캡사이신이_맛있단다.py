# https://www.acmicpc.net/problem/15824

import sys

input = sys.stdin.readline
MOD = 1000000007


def power(a: int, b: int) -> int:
    result = 1

    while b:
        if b & 1:
            result = result * a % MOD
        b >>= 1
        a *= a
        a %= MOD

    return result


N = int(input())
arr = sorted(map(int, input().split()))
positive = negative = 0

for i in range(N):
    positive += arr[i] % MOD * power(2, i) % MOD
    negative += arr[i] % MOD * power(2, N - i - 1) % MOD

print((positive - negative) % MOD)
