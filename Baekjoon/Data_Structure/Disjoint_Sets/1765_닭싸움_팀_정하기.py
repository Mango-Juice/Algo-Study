import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
friendship = [ i for i in range(n + 1) ]
enemy = [[] for _ in range(n + 1)]


def find(a):
    if a == friendship[a]:
        return a
    
    friendship[a] = find(friendship[a])
    return friendship[a]


def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        friendship[a] = b
    else:
        friendship[b] = a


for _ in range(m):
    c, p, q = input().split()
    p, q = int(p), int(q)
    
    if c == "F":
        union(p, q)
    else:
        for friend in enemy[p]:
            union(friend, q)
        for friend in enemy[q]:
            union(friend, p)
            
        enemy[p].append(q)
        enemy[q].append(p)

print(len(set(friendship)) - 1)