# https://www.acmicpc.net/problem/1976

import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)

def find(x: int) -> int:
    if tree[x] == '':
        return x
    tree[x] = find(tree[x])
    return tree[x]

def union(x: int, y: int) -> None:
    x = find(x)
    y = find(y)
    if x != y:
        tree[x] = y

n = int(input())
m = int(input())
tree = defaultdict(str)
answer = True
last = None

for i in range(n):
    for j, data in enumerate(map(int, sys.stdin.readline().split())):
        if data == 1:
            union(i + 1, j + 1)

for i in map(int, sys.stdin.readline().split()):
    if last != None:
        answer &= find(last) == find(i)
    last = i

print("YES" if answer else "NO")
