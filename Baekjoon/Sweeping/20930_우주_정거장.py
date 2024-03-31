import sys
input = sys.stdin.readline
sys.setrecursionlimit(200001)

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
x_arr = []
y_arr = []

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x_arr.append((*sorted([x1, x2]), i))
    y_arr.append((*sorted([y1, y2]), i))

disjoint = [i for i in range(n)]
x_arr.sort()
y_arr.sort()

lr, lt = x_arr[0][1:]
for i in range(n):
    l, r, t = x_arr[i]
    
    if l <= lr:
        lr = max(lr, r)
        union(lt, t)
    else:
        lr = r
        lt = t

lr, lt = y_arr[0][1:]
for i in range(n):
    l, r, t = y_arr[i]
    
    if l <= lr:
        lr = max(lr, r)
        union(lt, t)
    else:
        lr = r
        lt = t

for _ in range(q):
    print(int(is_same(*map(int, input().split()))))