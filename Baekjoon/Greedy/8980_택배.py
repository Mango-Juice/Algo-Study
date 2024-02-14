import sys
input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())
posts = [list(map(int, input().split())) for _ in range(m)]
posts.sort(key=lambda x: (x[1], x[0]))

capacity = [c] * (n + 1)
answer = 0
for start, end, weight in posts:
    target = min(*capacity[start:end], weight)
    for i in range(start, end): capacity[i] -= target
    answer += target

print(answer)