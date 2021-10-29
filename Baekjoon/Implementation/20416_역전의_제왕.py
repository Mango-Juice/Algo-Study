# https://www.acmicpc.net/problem/20416

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
scores = [[0, 0, i] for i in range(N)]
grades = [0 for _ in range(N)]
xRPs = [0 for _ in range(N)]
flag = False
arr = [[] for _ in range(N)]

for _ in range(M):
    inp = input().split()
    tmp = inp[0].split(':')
    time = int(tmp[0]) * 60 + int(tmp[1])
    
    if time <= 180:
        scores[int(inp[1]) - 1][0] -= 1
        scores[int(inp[1]) - 1][1] += time + 20 * (int(inp[3]) - 1)
        
    else:
        if not flag:
            flag = True
            scores.sort()
            for i in range(N): grades[scores[i][2]] = i

        arr[int(inp[1]) - 1].append((int(inp[2]), time, inp))

for i in arr: i.sort()

while True:
    flag1 = False
    
    for i in reversed(scores):
        idx = i[2]
        if not arr[idx]: continue
        flag1, flag2 = True, False

        while arr[idx]:
            _, time, inp = arr[idx].pop(0)
            target = grades[int(inp[1]) - 1]
            scores[target][0] -= 1
            scores[target][1] += time + 20 * (int(inp[3]) - 1)

            while target > 0 and scores[target] < scores[target - 1]:
                flag2 = True
                xRPs[int(inp[1]) - 1] += 1
                grades[scores[target - 1][2]], grades[int(inp[1]) - 1] = grades[int(inp[1]) - 1], grades[scores[target - 1][2]]
                scores[target], scores[target - 1] = scores[target - 1], scores[target]
                target -= 1

            if flag2: break

        if flag2: break

    if not flag1: break
    
ranking = sorted([(-xRPs[i], grades[i], i + 1) for i in range(N)])
print(ranking[0][2])
