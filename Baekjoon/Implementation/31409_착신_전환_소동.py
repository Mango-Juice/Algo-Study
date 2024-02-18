import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

count = 0
for i in range(n):
    if arr[i] == i + 1:
        count += 1
        arr[i] = 1 if i > 0 else 2

print(count)
print(*arr)