# https://www.acmicpc.net/problem/17302

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
arr = []

def reverse(n, m):
    for dn, dm in DIRECTIONS:
        nn, nm = n + dn, m + dm
        if 0 <= nn < N and 0 <= nm < M:
            arr[nn][nm] = ('W' if arr[nn][nm] == 'B' else 'B')

for _ in range(N):
    arr.append(list(input().strip()))

for n in range(N):
    for m in range(M):
        reverse(n, m)

print(1)
for n in range(N):
    print(*map(lambda x : 3 if x == 'B' else 2, arr[n]), sep='')
