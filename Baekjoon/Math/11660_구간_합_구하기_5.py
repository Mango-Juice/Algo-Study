import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = [[0] * (N + 1)]

for _ in range(N):
    a.append([0] + list(map(int, input().split())))

for k1 in range(1, N + 1):
    for k2 in range(1, N + 1):
        a[k1][k2] += a[k1 - 1][k2] + a[k1][k2 - 1] - a[k1 - 1][k2 - 1]

for _ in range(M):
    i1, i2, j1, j2 = map(int, input().split())
    print(a[j1][j2] - a[i1 - 1][j2] - a[j1][i2 - 1] + a[i1 - 1][i2 - 1])