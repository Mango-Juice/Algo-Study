# https://www.acmicpc.net/problem/18429

def sol(status: int, result: set[int]) -> int:
    if len(result) == N: return 1

    answer = 0
    
    for i in set(range(N)) - result:
        if status - K + arr[i] >= 500:
            answer += sol(status - K + arr[i], result | {i})

    return answer
    
    
N, K = map(int, input().split())
arr = list(map(int, input().split()))

print(sol(500, set()))
