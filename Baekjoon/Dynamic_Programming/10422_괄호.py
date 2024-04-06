import sys
input = sys.stdin.readline
sys.setrecursionlimit(5001)

MOD = 1000000007
arr = [None] * 5001
arr[0] = arr[2] = 1

def get(n):
    if n & 1: return 0
    if arr[n] != None: return arr[n]
    
    arr[n] = 0
    for i in range(0, n, 2):
        arr[n] = (arr[n] + get(i) * get(n - i - 2)) % MOD
    return arr[n]

t = int(input())
for _ in range(t):
    print(get(int(input())))