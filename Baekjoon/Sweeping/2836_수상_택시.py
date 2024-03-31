import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

for _ in range(n):
    a, b = map(int, input().split())
    if a > b: arr.append((b, a))

if not arr:
    print(m)
    exit()

arr.sort()
answer = 0
ll, lr = arr[0]

for i in range(1, len(arr)):
    l, r = arr[i]
    
    if l <= lr:
        lr = max(lr, r)
    else:
        answer += lr - ll
        ll, lr = l, r

print(m + (answer + lr - ll) * 2)