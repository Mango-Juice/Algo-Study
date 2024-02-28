import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key = lambda x: (x[1], x[0]))

count = 0
last = -1
for start, finish in arr:
    if start >= last:
        count += 1
        last = finish

print(count)