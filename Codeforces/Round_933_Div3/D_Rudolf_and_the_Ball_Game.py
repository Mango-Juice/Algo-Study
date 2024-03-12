import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def solve(pos, count):
    global n, m, arr, dp
    if count == m: return [pos]
    if dp[pos][count]: return []
    dp[pos][count] = True
    
    num, data = arr[count]
    result = []
    if data == "0" or data == "?":
        val = pos + num
        if val > n: val -= n
        result.extend(solve(val, count + 1))
    if data == "1" or data == "?":
        val = pos - num
        if val < 1: val = n + val
        result.extend(solve(val, count + 1))
    
    return result


t = int(input())
for _ in range(t):
    n, m, x = map(int, input().split())
    arr = []
    dp = [[False] * m for _ in range(n + 1)]
    
    for _ in range(m):
        num, data = input().split()
        arr.append((int(num), data))
    
    ans = set(solve(x, 0))
    print(len(ans))
    print(*sorted(ans))