# MST에 가상의 노드 하나 추가
import sys, heapq
input = sys.stdin.readline

def find(x):
    if x != arr[x]:
        arr[x] = find(arr[x])
    return arr[x]

def union(x, y):
    x = find(x)
    y = find(y)
    arr[max(x, y)] = min(x, y)


graph = []
n = int(input())

for i in range(n):
    heapq.heappush(graph, (int(input()), n, i))

for i in range(n):
    for j, c in enumerate(map(int, input().split())):
        heapq.heappush(graph, (c, i, j))

arr = [i for i in range(n + 1)]
answer = 0
while graph:
    c, i, j = heapq.heappop(graph)
    if find(i) != find(j):
        union(i, j)
        answer += c
    
    if len(set(arr)) == 1: break

print(answer)