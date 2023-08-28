import sys
input = sys.stdin.readline
POW_MAX = 20

m = int(input())
f = [[0] + list(map(int, input().split()))] + [[0] * (m + 1) for _ in range(POW_MAX  + 1)]

for pow in range(1, POW_MAX + 1):
    for node in range(m + 1):
        f[pow][node] = f[pow - 1][f[pow - 1][node]]

q = int(input())
for _ in range(q):
    n, x = map(int, input().split())
    
    for pow in range(POW_MAX, -1, -1):
        value = 2 ** pow
        if n >= value:
            n -= value
            x = f[pow][x]
    
    print(x)
