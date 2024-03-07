from collections import deque

n, k = map(int, input().split())
arr = list(map(int, input().split()))

now = answer = sum(arr[:k])

for i in range(k, n):
    now = now - arr[i - k] + arr[i]
    answer = max(answer, now)

print(answer)