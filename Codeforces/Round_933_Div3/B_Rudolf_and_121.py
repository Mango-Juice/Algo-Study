import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    flag = False
    for i in range(n - 2):
        arr[i + 1] -= arr[i] * 2
        arr[i + 2] -= arr[i]
        arr[i] = 0
        
        if arr[i + 1] < 0 or arr[i + 2] < 0:
            flag = True
            break
    
    if flag or arr[0] != 0 or len(set(arr)) > 1:
        print("NO")
    else:
        print("YES")