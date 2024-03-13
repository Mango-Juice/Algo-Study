
import sys
from bisect import bisect_left
input = sys.stdin.readline

def find_comb(group, now, end, cha, status, count):
    if now == end:
        group[count].append((cha, status))
        return
    
    find_comb(group, now + 1, end, cha + scores1[now], status, count + 1)
    find_comb(group, now + 1, end, cha - scores2[now], status | (1 << end - now - 1), count)


n = int(input())
scores1 = list(map(int, input().split()))
scores2 = list(map(int, input().split()))

half = n // 2 + 1
group1 = [[] for _ in range(half)]
group2 = [[] for _ in range(half)]
find_comb(group1, 0, n // 2, 0, 0, 0)
find_comb(group2, n // 2, n, 0, 0, 0)

for i in range(half):
    new_row = []
    last = None

    for cha, status in sorted(group2[i]):
        if last == cha: continue
        new_row.append((cha, status))
        last = cha

    group2[i] = new_row

ans, val = float('inf'), float('inf')
for i in range(half):
    for cha1, status1 in group1[i]:
        reverse = n // 2 - i
        target = bisect_left(group2[reverse], (-cha1, 0))
        cha, status = float('inf'), float('inf')
        
        if target < len(group2[reverse]):
            cha2, status2 = group2[reverse][target]
            cha, status = abs(cha1 + cha2), status2 | (status1 << (n // 2))
        
        if target > 0:
            cha2, status2 = group2[reverse][target - 1]
            cha_, status_ = abs(cha1 + cha2), status2 | (status1 << (n // 2))
            if cha_ < cha or (cha_ == cha and status_ < status):
                cha, status = cha_, status_
        
        if cha < val:
            val = cha
            ans = status
        elif cha == val and status < ans:
            ans = status

print(*[2 if ans & (1 << i) else 1 for i in range(n - 1, -1, -1)])