import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = []

for i in range(n):
    inp = list(map(int, input().split()))
    for a in inp:
        arr.append((a, i))

arr.sort()

l = r = 0
ans = float('inf')
types = 1
counts = [0] * n
counts[arr[0][1]] = 1

while r < n * k and l < n * k:
    if types == n:
        ans = min(ans, arr[r][0] - arr[l][0])
        counts[arr[l][1]] -= 1
        if counts[arr[l][1]] == 0: types -= 1
        l += 1
    else:
        r += 1
        if r == n * k: break
        counts[arr[r][1]] += 1
        if counts[arr[r][1]] == 1: types += 1

print(ans)