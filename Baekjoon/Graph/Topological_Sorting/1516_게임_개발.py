# https://www.acmicpc.net/problem/1516

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
cost = []
jinip = []
result = []
connection = [[] for _ in range(N)]

nxt = deque()

for i in range(N):
    inp = list(map(int, input().split()))
    cost.append(inp[0])
    result.append(inp[0])
    jinip.append(len(inp) - 2)
    
    if jinip[i] == 0:
        nxt.append(i)
    
    for j in range(1, len(inp) - 1):
        connection[inp[j] - 1].append(i)

while nxt:
    target = nxt.popleft()
    
    for i in connection[target]:
        jinip[i] -= 1
        result[i] = max(result[target] + cost[i], result[i])
        
        if jinip[i] == 0:
            nxt.append(i)

print(*result, sep = '\n')
