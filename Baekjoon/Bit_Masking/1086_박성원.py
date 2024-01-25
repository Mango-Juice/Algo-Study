import sys
from math import gcd, factorial
input = sys.stdin.readline

n = int(input())
nums = []
lens = []

for i in range(n):
    inp = input().strip()
    nums.append(int(inp))
    lens.append(len(inp))
    
k = int(input())

dp = [[-1] * k for _ in range(1 << n)]
remains = [[-1] * sum(lens) for _ in range(n)]

for i in range(n):
    for j in range(sum(lens)):
        remains[i][j] = (nums[i] * 10 ** j) % k

def find_answer(length: int, status: int, value: int):
    if status == (1 << n) - 1:
        return value % k == 0
    
    if dp[status][value] >= 0:
        return dp[status][value]
        
    dp[status][value] = 0
    for i in range(n):
        new_status = status | (1 << i)
        if new_status == status:
            continue

        dp[status][value] += find_answer(length + lens[i], new_status, (value + remains[i][length]) % k)
    
    return dp[status][value]

parent = factorial(n)
child = find_answer(0, 0, 0)

if child == 0:
    print("0/1")
elif child == parent:
    print("1/1")
else:
    gcd_num = gcd(parent, child)
    print(f"{child//gcd_num}/{parent//gcd_num}")