import sys
input = sys.stdin.readline
MOD = 1000000007
MAX = 101

n, l, r = map(int, input().split())
dp = [[[None] * MAX for _ in range(MAX)] for _ in range(MAX)]
dp[1][1][1] = 1

def solve(count, left, right):
    if left + right > count + 1 or left < 1 or right < 1 or count < 1:
        return 0
    if dp[left][right][count] is not None:
        return dp[left][right][count]
    
    dp[left][right][count] = solve(count - 1, left - 1, right) % MOD
    dp[left][right][count] = (dp[left][right][count] + solve(count - 1, left, right - 1)) % MOD
    dp[left][right][count] = (dp[left][right][count] + solve(count - 1, left, right) * (count - 2)) % MOD
    
    return dp[left][right][count]

print(solve(n, l, r))