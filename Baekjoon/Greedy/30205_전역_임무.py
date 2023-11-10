import sys
input = sys.stdin.readline

N, M, P = map(int, input().split())
success = True

for _ in range(N):
    s = list(map(int, input().split()))
    
    if not success:
        continue
    
    s.sort()
    minus = 0
    
    for value in s:
        if value == -1:
            minus += 1
        else:
            if value <= P:
                P += value
            else:
                while minus and value > P:
                    P *= 2
                    minus -= 1
                
                if value > P:
                    success = False
                else:
                    P += value
    
    while minus:
        P *= 2
        minus -= 1

print(int(success))