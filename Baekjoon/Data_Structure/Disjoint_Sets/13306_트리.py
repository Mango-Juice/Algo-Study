# Disjoint Set + Offline Query
import sys
input = sys.stdin.readline
sys.setrecursionlimit(200000)

# 상수
REMOVE, ASK = 0, 1

# 변수
n, q = map(int, input().split())
tree = [-1, 1]

querys = []
removed = [False] * (n + 1)
dset = [i for i in range(n + 1)]
rank = [0] * (n + 1)

answers = []


# 경로 압축 Find
def find(a):
    if dset[a] == a:
        return a
    
    dset[a] = find(dset[a])
    return dset[a]


# Union by Rank
def union(a, b):
    ra = find(a)
    rb = find(b)
    
    if ra == rb:
        return
    
    if rank[ra] == rank[rb]:
        dset[min(ra, rb)] = max(ra, rb)
        rank[max(ra, rb)] += 1
    elif rank[ra] > rank[rb]:
        dset[rb] = ra
    else:
        dset[ra] = rb


# 입력
for _ in range(n - 1):
    tree.append(int(input()))

for _ in range(n - 1 + q):
    query = list(map(int, input().split()))
    querys.append(query)
    
    if query[0] == REMOVE: # 지워졌는지 체크
        removed[query[1]] = True

# 안지워진 노드들 연결
for i in range(1, n + 1):
    if not removed[i]:
        union(tree[i], i)

# 쿼리 역순 진행
for query in querys[::-1]:
    if query[0] == REMOVE: # 역순이므로 제거가 아닌 연결 수행
        union(tree[query[1]], query[1])
    else:
        answers.append('YES' if find(query[1]) == find(query[2]) else 'NO')

# 출력
print(*answers[::-1], sep='\n')
