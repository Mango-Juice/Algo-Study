import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split())) + [float('inf')]
arr.sort()
answer = 0

for i in range(n):
    ok = False
    
    for j in range(n):
        if i == j: continue
    
        left = arr[i] - arr[j]
        pos = bisect_left(arr, left)
        
        while pos == i or pos == j: pos += 1
        if arr[pos] == left:
            ok = True
            break
    
    if ok: answer += 1

print(answer)