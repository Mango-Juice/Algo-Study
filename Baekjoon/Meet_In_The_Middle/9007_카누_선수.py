import sys
from bisect import bisect_left
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k, n = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(4)]
    
    g1 = []
    g2 = []
    for i in range(n):
        for j in range(n):
            g1.append(arr[0][i] + arr[1][j])
            g2.append(arr[2][i] + arr[3][j])
    
    g1.sort()
    g2.sort()
    answer = float("inf")
    for hap1 in g1:
        target_number = k - hap1
        index = bisect_left(g2, target_number)
        target = -float("inf")
        
        if index > 0:
            target = g2[index - 1]
        if index < n * n and target_number - target > g2[index] - target_number:
            target = g2[index]

        cha = target - target_number
        if abs(cha) < abs(answer) or (abs(cha) == abs(answer) and cha < answer):
            answer = cha
    
    print(answer + k)