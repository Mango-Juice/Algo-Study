# https://www.acmicpc.net/problem/20665

import sys
input = sys.stdin.readline

MAX = 501
N, T, P = map(int, input().split())
clients = []

for _ in range(T):
    clients.append(tuple(map(lambda x : int(x) - 900, input().split())))

clients.sort()
seats = [[False for _ in range(1201)] for _ in range(N + 1)]


def get_min_dist(idx, time):
    result = MAX

    for i in range(idx + 1, N):
        if seats[i][time]:
            result = i - idx
            break

    for i in range(idx, -1, -1):
        if seats[i][time]:
            result = min(result, idx - i)
            break

    return result


for f, t in clients:
    dist = [get_min_dist(i, f) for i in range(N)]
    target_idx = target_val = -1

    for i, v in enumerate(dist):
        if target_val < v:
            target_val = v
            target_idx = i
        
    for i in range(f, t):
        seats[target_idx][i] = True

answer = 0
for i in range(1200):
    if i % 100 >= 60:
        continue
    if not seats[P - 1][i]:
        answer += 1
print(answer)
