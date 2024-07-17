import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b = [max(-b[i], a[i] - 100) for i in range(m)]
arr = list(zip(b, range(m)))

heapq.heapify(arr)
now = sum(a)

for _ in range(n * 24):
    target = heapq.heappop(arr)
    now -= target[0]
    a[target[1]] -= target[0]
    
    heapq.heappush(arr, (max(target[0], a[target[1]] - 100), target[1]))
    
    if now == 100 * m:
        break

print(now)