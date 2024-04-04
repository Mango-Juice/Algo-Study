import sys
from collections import Counter, deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

counter = Counter(arr)
counter_arr = [(counter[arr[i]], arr[i], i) for i in range(n)]

answer = [-1] * n 
stack = deque([counter_arr[0]])
for i in range(1, n):
    now_count, now_number, _ = counter_arr[i]
    
    while stack and now_count > stack[-1][0]:
        _, _, index = stack.pop()
        answer[index] = now_number
    stack.append(counter_arr[i])

print(*answer)