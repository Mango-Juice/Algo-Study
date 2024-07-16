from itertools import combinations

v, p, l = map(int, input().split())
arr = tuple(map(int, input().split()))

def get_cost(target):
    cost = 0
    for i in arr:
        now = float('inf')
        for j in target:
            now = min(now, abs(i - j), l - abs(i - j))
        cost += now
    return cost


minimum = float('inf')
answer = []

for c in combinations(arr, p):
    cost = get_cost(c)
    
    if cost < minimum:
        minimum = cost
        answer = c

print(minimum)
print(*answer)