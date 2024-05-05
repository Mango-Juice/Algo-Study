import sys
input = sys.stdin.readline

def find(x):
    if x != arr[x]:
        arr[x] = find(arr[x])
    return arr[x]


def union(x, y):
    x = find(x)
    y = find(y)
    arr[max(x, y)] = min(x, y)


n, m = map(int, input().split())
graphs = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graphs.append((c, a, b))

graphs.sort()
arr = [i for i in range(n + 1)]
mst_graphs = []

for c, a, b in graphs:
    if find(a) != find(b):
        union(a, b)
        mst_graphs.append((c, a, b))

q = int(input())
for _ in range(q):
    result = 0
    arr = [i for i in range(n + 1)]
    union(*map(int, input().split()))
    
    for c, a, b in mst_graphs:
        if find(a) != find(b):
            union(a, b)
            result += c
    
    print(result)