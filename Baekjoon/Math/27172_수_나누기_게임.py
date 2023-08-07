import sys
input = sys.stdin.readline

n = int(input())
arr = tuple(map(int, input().split()))
limit = max(arr) + 1
chae = [0] * limit
hasNum = [False] * limit

for i in arr:
    hasNum[i] = True

for i in sorted(arr):
    for j in range(i * 2, limit, i):
        if hasNum[j]:
            chae[i] += 1
            chae[j] -= 1

print(*map(lambda x : chae[x], arr))
