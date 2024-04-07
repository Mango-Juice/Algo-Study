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
types = " " + input().rstrip()

arr = [i for i in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    if types[a] == types[b]:
        union(a, b)

for _ in range(m):
    a, b, t = input().split()
    a, b = find(int(a)), find(int(b))
    print(int(a != b or t == types[a]), end="")