# https://www.acmicpc.net/problem/17301

import sys
input = sys.stdin.readline

N = int(input())
MOD = 1000000007

dp = [1] * (N + 1)
n = c = 0
cn = 1

for _ in range(N):
    inp = input()
    n_idx = inp.find('N')
    c_idx = inp.rfind('C')

    if n_idx == -1: c += 1
    elif c_idx == -1: n += 1
    elif c_idx < n_idx: cn += 1


for i in range(1, N + 1):
    dp[i] = (i * dp[i - 1] + 1) % MOD

print((dp[N] - (cn * dp[n] * dp[c]) % MOD) % MOD)
