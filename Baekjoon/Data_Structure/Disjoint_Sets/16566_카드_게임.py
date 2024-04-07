# https://www.acmicpc.net/problem/16566
# Union-Find

import sys, bisect

sys.setrecursionlimit(10 ** 7)

def find(x):
    if tree[x] == x:
        return x
    tree[x] = find(tree[x])
    return tree[x]

def union(x, y):
    tree[find(x)] = find(y)

n, m, k = map(int, sys.stdin.readline().split())
tree = [i for i in range(n + 1)]
cards = sorted(map(int, sys.stdin.readline().split()))
chulsu = list(map(int, sys.stdin.readline().split()))

for i in chulsu:
    target = find(bisect.bisect(cards, i))
    print(cards[target])
    union(target, target + 1)
