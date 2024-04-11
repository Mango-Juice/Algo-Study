import sys, math
input = sys.stdin.readline

n = int(input())
arr = [0] * (n + 1)
arr[0] = 1

for i in range(1, n + 1):
    if i & 1:
        arr[i] = arr[i - 1]
    else:
        arr[i] = (arr[i - 1] + arr[i >> 1]) % 1000000000

print(arr[n])