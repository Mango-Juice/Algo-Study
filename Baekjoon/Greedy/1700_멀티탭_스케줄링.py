import sys
input = sys.stdin.readline

def get_useless(i):
    useless = useless_value = -1
    
    for target in now:
        if not positions[target]:
            return target
        
        next_position = bisect(positions[target], i)
        if next_position >= len(positions[target]):
            return target
        if positions[target][next_position] > useless_value:
            useless = target
            useless_value = positions[target][next_position]

    return useless


n, k = map(int, input().split())
arr = list(map(int, input().split()))

positions = [[] for _ in range(101)]
for i in range(k):
    positions[arr[i]].append(i)

now = set()
count = 0
for i in range(k):
    if not arr[i] in now and len(now) >= n:
        count += 1
        now.remove(get_useless(i))
    now.add(arr[i])

print(count)