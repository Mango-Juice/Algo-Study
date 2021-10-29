# https://www.acmicpc.net/problem/20413

N = int(input())
s, g, p, d = map(int, input().split())
mvp = input()

cost = { 'B': s, 'S': g, 'G': p, 'P': d }
answer = last = 0

for i in mvp:
    if i == 'D':
        answer += d
        last = d
    else:
        answer += cost[i] - 1 - last
        last = cost[i] - 1 - last

print(answer)
