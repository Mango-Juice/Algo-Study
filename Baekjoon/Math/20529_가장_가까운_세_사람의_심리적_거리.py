import sys
input = sys.stdin.readline

def distance(*args):
    if len(args) == 3:
        return distance(args[0], args[1]) + distance(args[1], args[2]) + distance(args[2], args[0])
    
    a, b = args
    result = 0
    for i in range(4):
        if a[i] != b[i]:
            result += 1
    
    return result


T = int(input())
for _ in range(T):
    N = int(input())
    arr = input().split()
    
    if N > 32:
        print(0)
        continue
    
    answer = float('inf')
    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            for k in range(j + 1, N):
                answer = min(answer, distance(arr[i], arr[j], arr[k]))
    
    print(answer)