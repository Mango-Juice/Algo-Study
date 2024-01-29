import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    answer = 1
    
    for _ in range(b):
        answer = (answer * a) % 10
    
    print(10 if answer == 0 else answer)
