# https://www.acmicpc.net/problem/9527

import sys
input = sys.stdin.readline

def hap(target: int) -> int:
    result = target & 1;
    
    for i in range(54, 0, -1):
        if target & (1 << i):
            result += dp[i - 1] + (target - (1 << i) + 1)
            target -= 1 << i

    return result

dp = []
dp.append(1)

for i in range(55):
    dp.append(dp[i] * 2 + (1 << (i + 1)))

a, b = map(int, input().split())
print(hap(b) - hap(a - 1))
