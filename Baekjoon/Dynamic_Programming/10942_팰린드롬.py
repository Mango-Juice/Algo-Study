#https://www.acmicpc.net/problem/10942

import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
dp = [[None for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = True
    if i < n - 1 and nums[i] == nums[i + 1]:
        dp[i][i + 1] = True

for _ in range(m):
    left, right = map(int, sys.stdin.readline().split())
    l, r = left - 1, right - 1
    new_data = []
    answer = None
    
    while answer == None:
        if dp[l][r] != None:
            answer = dp[l][r]
        elif nums[l] != nums[r]:
            dp[l][r] = False
            answer = False
        else:
            new_data.append((l, r))
            l += 1
            r -= 1

    for ld, rd in new_data:
        dp[ld][rd] = answer
    
    print(int(answer))
