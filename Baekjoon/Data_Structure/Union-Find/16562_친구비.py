import sys
input = sys.stdin.readline

def find(x):
    if x != friends[x]:
        friends[x] = find(friends[x])
    return friends[x]


def union(a, b):
    a = find(a)
    b = find(b)
    friends[max(a, b)] = min(a, b)


n, m, k = map(int, input().split())
costs = tuple(map(int, input().split()))

friends = [i for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

total = {}
for i in range(1, n + 1):
    root = find(i)
    if root in total:
        total[root] = min(total[root], costs[i - 1])
    else:
        total[root] = costs[i - 1]

answer = sum(total.values())
print(answer if answer <= k else "Oh no")