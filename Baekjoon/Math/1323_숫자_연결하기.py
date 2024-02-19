n, k = map(int, input().split())

now = n
length = len(str(n))
visited = [False] * k

for i in range(k + 1):
    mod = now % k
    
    if mod == 0:
        print(i + 1)
        break
    
    if visited[mod]:
        print(-1)
        break
    
    visited[mod] = True
    now = mod * (10 ** length) + n