import sys
input = sys.stdin.readline

def find(x):
    if x != disjoint[x]:
        disjoint[x] = find(disjoint[x])
    return disjoint[x]


def union(x, y):
    x = find(x)
    y = find(y)
    disjoint[max(x, y)] = min(x, y)


def is_same(x, y):
    return find(x - 1) == find(y - 1)


n, q = map(int, input().split())
arr = []

for i in range(n):
    x1, x2, _ = map(int, input().split())
    arr.append((x1, x2, i))

arr.sort()
disjoint = [i for i in range(n)]
lr, lt = arr[0][1:]

for i in range(1, n):
    l, r, t = arr[i]
    
    if l <= lr:
        lr = max(lr, r)
        union(lt, t)
    else:
        lr = r
        lt = t

for _ in range(q):
    print(int(is_same(*map(int, input().split()))))