import sys, math
input = sys.stdin.readline

n, m = map(int, input().split())
inp = list(map(int, input().split()))

neg, pos = [], []
for i in inp:
    if i < 0: neg.append(i)
    else: pos.append(i)

neg.sort()
pos.sort(reverse=True)

answer = maximum = 0
for i in range(0, math.ceil(len(neg) / m) * m, m):
    answer += neg[i] * -2
    maximum = max(maximum, -neg[i])

for j in range(0, math.ceil(len(pos) / m) * m, m):
    answer += pos[j] * 2
    maximum = max(maximum, pos[j])

print(answer - maximum)