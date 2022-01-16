import sys
input = sys.stdin.readline

MAX = 10 ** 9 + 1
N = int(input())
roads = []

for _ in range(N):
    roads.append(tuple(map(int, input().split())))

roads.sort()
last_l = last_r = 0
max_idx = 0
answer = 0

for l, r in roads:
    if l <= last_r:
        if r <= last_r:
            continue
        max_idx = max(max_idx, 2 * r - last_l)

    else:
        if max_idx < l:
            break
        max_idx = max(max_idx, 2 * r - l)
        last_l = l

    last_r = r
    answer = max(r, answer)

    # print(l, r, max_idx)

print(answer)
