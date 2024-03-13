from collections import deque

t = int(input())

for _ in range(t):
    n, m, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    count = 0
    now = sum(arr[n - m:])
    
    if n == m:
        print(int(now < k))
        continue
    
    for i in range(n):
        now = now - arr[i - m] + arr[i]
        if now < k: count += 1
    
    print(count)