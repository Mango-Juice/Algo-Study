#https://www.acmicpc.net/problem/11066

import sys

t = int(sys.stdin.readline())

for _ in range(t):
    answer = float('inf')
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    memo = [[-1 for _ in range(n)] for _ in range(n)]
    part_sum, last = [0], 0

    for i in arr:
        last += i
        part_sum.append(last)
    
    def dp(f: int, t: int) -> int:
        if f == t:
            return arr[f]
        if memo[f][t] != -1:
            return memo[f][t]

        result = float('inf')

        for i in range(f, t):
            result = min(result, dp(f, i) + dp(i + 1, t) + part_sum[t + 1] - part_sum[f])

        memo[f][t] = result
        return result
    
    for i in range(n - 1):
        answer = min(answer, dp(0, i) + dp(i + 1, n - 1))

    print(answer)
