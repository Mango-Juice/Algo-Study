import sys
input = sys.stdin.readline

n = int(input())
a, b, c, d = [], [], [], []

for _ in range(n):
    ai, bi, ci, di = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)
    d.append(di)

targets = {}

for ai in a:
    for bi in b:
        targets[ai + bi] = targets.get(ai + bi, 0) + 1

answer = 0
for ci in c:
    for di in d:
        target = -(ci + di)
        if target in targets:
            answer += targets[target]

print(answer)