# https://www.acmicpc.net/problem/5569

MOD, NORTH, EAST = 100000, 0, 1
w, h = map(int, input().split())
arr = [[[[0, 0], [0, 0]] for _ in range(w + 1)] for _ in range(h + 1)]
# arr[h][w][방향][방향 전환 가능 여부]

for i in range(2, h + 1): arr[i][1][NORTH][True] = 1
for i in range(2, w + 1): arr[1][i][EAST][True] = 1

for i in range(2, h + 1):
    for j in range(2, w + 1):
        arr[i][j][NORTH][True] = sum(arr[i - 1][j][NORTH]) % MOD
        arr[i][j][EAST][True] = sum(arr[i][j - 1][EAST]) % MOD
        arr[i][j][NORTH][False] = arr[i - 1][j][EAST][True] % MOD
        arr[i][j][EAST][False] = arr[i][j - 1][NORTH][True] % MOD

print((arr[i][j][NORTH][True] + arr[i][j][EAST][True] + arr[i][j][NORTH][False] + arr[i][j][EAST][False]) % MOD)
