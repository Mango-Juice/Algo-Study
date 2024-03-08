import sys
input = sys.stdin.readline

# 문자 -> 숫자 변환 함수
def atoi(c):
    if c == '0': return 0
    if ord(c) < ord('a'): return ord(c) - ord('A') + 27
    return ord(c) - ord('a') + 1


def find(x):
    if parent[x] == x: return x
    parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    parent[max(x, y)] = min(x, y)


n = int(input())
parent = [i for i in range(n)]

total = 0
graphs = []

# 입력 처리
for i in range(n):
    for j, w in enumerate(map(atoi, input().strip())):
        if w == 0: continue
        graphs.append((w, i, j))
        total += w

# 크루스칼 알고리즘
graphs.sort()

for w, f, t in graphs:
    f, t = find(f), find(t)
    
    if f != t:
        union(f, t)
        total -= w

# 연결 체크
now = find(0)
for i in range(1, n):
    if find(i) != now:
        print(-1)
        exit()

print(total)