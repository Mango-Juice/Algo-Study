import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = list(map(int, input().split()))
t = [list(map(int, input().split())) for _ in range(n)]

dp = [(0, -1)] * (m + 1)
answer = -1

for i in range(n):
    for index, value in enumerate(t[i]):
        last_dp = dp.copy()
        
        for j in range(m - value + 1):
            target_value, target_index = dp[j]
            
            if target_index < i - 1:
                continue
            
            last_dp[target_value + value] = (target_value + value, i)
            
        dp = last_dp

for value, index in dp[::-1]:
    if index == n - 1:
        answer = value
        break

print(answer)