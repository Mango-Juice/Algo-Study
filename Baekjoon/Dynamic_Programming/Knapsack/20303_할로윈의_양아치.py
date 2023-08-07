# 1차원 배열을 활용한 냅색 + 서로소집합

from collections import defaultdict
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
candies = tuple(map(int, input().split()))
friendship = [i for i in range(n + 1)]

def find(a):
    if friendship[a] != a:
        return find(friendship[a])
    return friendship[a]
    
def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        friendship[b] = a
    else:
        friendship[a] = b

# 친구 관계 정립
for i in range(m):
    a, b = map(int, input().split())
    union(a, b)

# 사탕, 울음 수 집계
candy = defaultdict(int)
cry = defaultdict(int)
for i in range(1, n + 1):
    friend = find(i)
    cry[friend] += 1
    candy[friend] += candies[i - 1]

data = []
for key, value in candy.items():
    data.append((cry[key], value))


# 냅색
dp = [0] * k
for cost, value in data:
    for limit in range(k - 1, cost - 1, -1):
        dp[limit] = max(dp[limit], dp[limit - cost] + value)


print(dp[k - 1])
