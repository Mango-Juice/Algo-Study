from collections import defaultdict

n, target = input().split()
n = int(n)

d = defaultdict(int)

for _ in range(n):
    a, b = input().split()
    if target == a:
        print(d[b])
        exit(0)
    d[b] += 1