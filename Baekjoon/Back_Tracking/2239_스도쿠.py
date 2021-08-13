# https://www.acmicpc.net/problem/2239

import sys

input = sys.stdin.readline

SIZE = 9

finish = False
arr = []
ud = [[False for _ in range(10)] for _ in range(SIZE)]
lr = [[False for _ in range(10)] for _ in range(SIZE)]
sq = [[False for _ in range(10)] for _ in range(SIZE)]

def get_sq_idx(i, j):
    return (i // 3) * 3 + j // 3

def dfs(count):
    global finish
    
    if count == 81:
        finish = True
        return
    
    x, y = divmod(count, SIZE)

    if arr[x][y] == 0:
        for i in range(1, 10):
            if (not ud[x][i]) and (not lr[y][i]) and (not sq[get_sq_idx(x, y)][i]):
                ud[x][i] = lr[y][i] = sq[get_sq_idx(x, y)][i] = True
                arr[x][y] = i
                dfs(count + 1)
                if not finish:
                    ud[x][i] = lr[y][i] = sq[get_sq_idx(x, y)][i] = False
                    arr[x][y] = 0
    else:
        dfs(count + 1)

for i in range(SIZE):
    inp = list(map(int, input().rstrip()))
    arr.append(inp)
    
    for j, val in enumerate(inp):
        if val != 0:
            ud[i][val] = True
            lr[j][val] = True
            sq[get_sq_idx(i, j)][val] = True

dfs(0)

for i in range(SIZE):
    print(*arr[i], sep = '')
