# https://www.acmicpc.net/problem/2193
# DP

n = int(input())
zero = 0
one = 1

for i in range(n - 1):
    zero, one = zero + one, zero

print(zero + one)
