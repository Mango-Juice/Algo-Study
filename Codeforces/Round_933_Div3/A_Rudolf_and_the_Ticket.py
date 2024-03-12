import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    answer = 0
    for i in b:
        for j in c:
            if i + j <= k:
                answer += 1
    
    print(answer)