import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
visited[1] = True
target = [1]

dist = answer = count = 0
while target:
    new_answer = float('inf')
    new_count = 0
    new_target = []
    
    for i in target:
        for j in graph[i]:
            if not visited[j]:
                visited[j] = True
                new_target.append(j)
                new_count += 1
                new_answer = min(new_answer, j)
    
    if new_count:
        count = new_count
        answer = new_answer
        dist += 1
    target = new_target

print(answer, dist, count)