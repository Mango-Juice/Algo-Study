import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def dist(a, b):
    ap = events[a] if a >= 0 else (1, 1)
    bp = events[b] if b >= 0 else (n, n)
    return abs(ap[0] - bp[0]) + abs(ap[1] - bp[1])


def solve(a, b):
    if a == w - 1 or b == w - 1:
        return 0
    
    if dp[a][b] > -1:
        return dp[a][b]
    
    x = max(a, b) + 1
        
    dp[a][b] = min(solve(x, b) + dist(a, x), solve(a, x) + dist(x, b))
    return dp[a][b]
    

def print_method(a, b):
    if a == w - 1 or b == w - 1:
        return
        
    x = max(a, b) + 1
    ad = solve(x, b) + dist(a, x)
    bd = solve(a, x) + dist(x, b)
    
    if ad < bd:
        print(1)
        print_method(x, b)
    else:
        print(2)
        print_method(a, x)


n = int(input())
w = int(input())
events = [tuple(map(int, input().split())) for _ in range(w)]
dp = [[-1] * w for _ in range(w)]

print(solve(-1, -1))
print_method(-1, -1)
