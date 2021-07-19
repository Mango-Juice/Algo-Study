# https://www.acmicpc.net/problem/11053

n = int(input())
an = list(map(int, input().split()))

dp = {}
answer = 0

def get_increasing_length(idx):
    if idx in dp:
        return dp[idx]

    last = an[idx]
    result = 1
    
    for i in range(idx + 1, n):
        if result > n - i:
            break
        if an[i] > last:
            result = max(get_increasing_length(i) + 1, result)

    dp[idx] = result
    return result

for i in range(n):
    if answer > n - i:
        break
    answer = max(get_increasing_length(i), answer)

print(answer)
