# https://www.acmicpc.net/problem/17307

import sys
input = sys.stdin.readline

N, C = map(int, input().split())
X = list(map(int, input().split()))

left = [0] * N
right = [0] * N
answer_idx, answer_val = -1, float('inf')

for i in range(1, N):
    cha = X[i - 1] - X[i]
    if cha < 0: cha += C
    left[i] = left[i - 1] + cha

for i in range(N - 2, -1, -1):
    cha = X[i + 1] - X[i]
    if cha < 0: cha += C
    right[i] = right[i + 1] + cha

    val = max(right[i], left[i])
    if val <= answer_val:
        answer_val = val
        answer_idx = i

if answer_val == float('inf'):
    answer_idx = 0
    answer_val = 0

print(answer_idx + 1)
print(answer_val)
