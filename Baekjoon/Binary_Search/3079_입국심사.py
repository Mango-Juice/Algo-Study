# https://www.acmicpc.net/problem/3079

import time
simsa = []

inp = input().split()
n = int(inp[0])
m = int(inp[1])

for i in range(n):
    simsa.append(int(input()))

##############################

max_ = min(simsa) * m
min_ = 0
target = 0
lastmax = 0
lastmin = 0

while True: #이분탐색
    inone = 0
    target = (max_ + min_) // 2

    if lastmin == min_ and lastmax == max_: #반복을 또해?
        target += 1 #어림도 없지!
        break
    
    for i in simsa:
        inone += target // i
    
    lastmax = max_
    lastmin = min_
    
    if inone >= m:
        max_ = target
    elif inone < m:
        min_ = target
    else:
        break
  
##############################
    
print(target)
