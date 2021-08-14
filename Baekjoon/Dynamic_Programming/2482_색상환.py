# https://www.acmicpc.net/problem/2482

# 상수
MOD = 1000000003

# 함수
def solution(n: int, k: int) -> int:
    if k <= 0 or n <= 0: return 0
    
    if dp[n][k] > -1: return dp[n][k]

    if k == 1: # k = 1이면 남은 색깔 수가 경우의 수임
        dp[n][k] = n
        return n
    
    if k * 2 > n + 1: # 남은 부분을 규칙대로 모두 선택해도 불가능 할 때
        dp[n][k] = 0
        return dp[n][k]

    dp[n][k] = (solution(n - 1, k) + solution(n - 2, k - 1)) % MOD
    
    return dp[n][k]

# 입력 및 초기화
N = int(input())
K = int(input())
dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]

# 출력
if K == 1:
    print(solution(N, K) % MOD)
else:
    print((solution(N - 1, K) + solution(N - 3, K - 1)) % MOD)
