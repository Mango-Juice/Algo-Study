# https://www.acmicpc.net/problem/10775

import sys

sys.setrecursionlimit(10 ** 5)

def find(x):
    if datas[x] == x:
        return x
    datas[x] = find(datas[x])
    return datas[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        datas[x] = y

gates = int(sys.stdin.readline())
planes = int(sys.stdin.readline())
datas = [i for i in range(gates + 1)]
flag = False

for i in range(planes):
    gi = int(sys.stdin.readline())
    root = find(gi)

    if root == 0:
        flag = True
        print(i)
        break

    union(gi, root - 1)
  
if not flag:
    print(planes)
