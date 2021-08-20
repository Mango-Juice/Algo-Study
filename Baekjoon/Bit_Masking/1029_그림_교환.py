# https://www.acmicpc.net/problem/1029

import sys
input = sys.stdin.readline

def solution(target: int, status: int, price: int) -> int:
    if dp[target][status][price] > -1:
        return dp[target][status][price]
    
    if status == (1 << n) - 1:
        dp[target][status][price] = 1
        return 1
    
    result = 1

    for i in range(n):
        if (status & (1 << i)) or i == target: continue
        if arr[target][i] >= price:
            result = max(result, solution(i, status | (1 << i), arr[target][i]) + 1)

    dp[target][status][price] = result

    return result


n = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
dp = [[[-1 for _ in range(10)] for _ in range(1 << n)] for _ in range(n)]

print(solution(0, 1, 0))
