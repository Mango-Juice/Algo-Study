# https://www.acmicpc.net/problem/14267

import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)
        

def dfs(idx: int) -> None:
    for i in arr[idx]:
        answer[i] += answer[idx]
        dfs(i)


n, m = map(int, input().split())
answer = [0 for i in range(n)]
arr = [[] for i in range(n)]

for idx, val in enumerate(map(int, input().split())):
    if val > 0:
        arr[val - 1].append(idx)

for _ in range(m):
    i, w = map(int, input().split())
    answer[i - 1] += w

dfs(0)

print(*answer)
