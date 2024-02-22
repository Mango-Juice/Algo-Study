import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
remainder = [0] * m

for i in range(1, n + 1):
    arr[i] = (arr[i] + arr[i - 1]) % m
    remainder[arr[i]] += 1

answer = remainder[0]
for i in range(m):
    answer += (remainder[i] * (remainder[i] - 1)) // 2

print(answer)