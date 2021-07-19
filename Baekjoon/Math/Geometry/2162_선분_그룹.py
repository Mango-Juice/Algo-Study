# https://www.acmicpc.net/problem/2162
# Union Find + CCW를 이용한 선분 교차 판정

import sys
from collections import Counter

sys.setrecursionlimit(10 ** 4)

def find(x: int) -> int:
    if tree[x] == -1:
        return x
    tree[x] = find(tree[x])
    return tree[x]

def union(x: int, y: int) -> None:
    x = find(x)
    y = find(y)

    if x != y:
        tree[x] = y

def ccw(a: tuple, b: tuple, c: tuple) -> int:
    value = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
    value -= a[1] * b[0] + b[1] * c[0] + c[1] * a[0]
    return 1 if value > 0 else -1 if value < 0 else 0

n = int(sys.stdin.readline())
lines = []
tree = [-1] * n
roots = []
answer = 0

for now_idx in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    for line_idx, tup in enumerate(lines):
        a, b, c, d = tup[0], tup[1], (x1, y1), (x2, y2)
        ab, cd = ccw(a, b, c) * ccw(a, b, d), ccw(c, d, a) * ccw(c, d, b)
        
        if ab == 0 and cd == 0:
            a, b = min(a, b), max(a, b)
            c, d = min(c, d), max(c, d)
            if c <= b and a <= d:
                union(now_idx, line_idx)
        elif ab <= 0 and cd <= 0:
            union(now_idx, line_idx)
        
    lines.append(((x1, y1), (x2, y2)))

for i in range(n):
    root = find(i)
    if root > -1:
        roots.append(root)

counter = Counter(roots)

print(len(counter))
print(counter.most_common()[0][1])
