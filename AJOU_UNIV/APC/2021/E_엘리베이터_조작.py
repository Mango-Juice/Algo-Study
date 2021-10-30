# E

from collections import deque
import sys
sys.setrecursionlimit(100001)

n = int(input())
arr = [-1 for _ in range(n)]
answer = []
cycle = [False for _ in range(n)]
inner = [0 for _ in range(n)]
iz = deque()

def find_cycle(idx):
    if cycle[idx]:
        answer.append(idx + 1)
        return

    cycle[idx] = True
    answer.append(idx + 1)
    find_cycle(arr[idx])
    
for idx, val in enumerate(map(int, input().split())):
    arr[idx] = val - 1
    inner[val - 1] += 1

for i in range(n):
    if inner[i] == 0: iz.append(i)

if not iz: iz.append(0)

while iz:
    target = iz.popleft()
    find_cycle(target)

for i in range(n):
    if not cycle[i]: find_cycle(i)

if answer[0] == 1: del answer[0]

print(len(answer))  
print(*answer)
