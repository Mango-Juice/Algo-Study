import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    visited = [False] * (n + 1)
    
    q = deque([1])
    visited[1] = True
    
    while q:
        num = q.popleft()
        
        if num % n == 0:
            print(num)
            break
        
        flag = False
        for next in (num * 10, num * 10 + 1):
            mod = next % n
            if not visited[mod]:
                q.append(next)
                visited[mod] = True
                if mod == 0:
                    print(next)
                    flag = True
                    break
        
        if flag:
            break