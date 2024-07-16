import sys
input = sys.stdin.readline

n = int(input())
arr = [0] + [int(input()) for _ in range(n)]

for i in range(1, n + 1):
    arr[i] += arr[i - 1]

l = r = 1
answer = last = 0

while r < n + 1:
    now = arr[r] - arr[l - 1]
    result = min(now, arr[n] - now)

    if result < last:
        l += 1
        r = l
        last = 0
    else:
        r += 1
        last = result
    
    answer = max(answer, result)

print(answer)