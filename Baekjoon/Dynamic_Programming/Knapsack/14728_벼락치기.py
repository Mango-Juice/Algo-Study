import sys
input = sys.stdin.readline

n, t = map(int, input().split())
studies = [list(map(int, input().split())) for _ in range(n)]
knapsack = [0] * (t + 1)

for time, score in studies:
    for j in range(t, 0, -1):
        if time <= j:
            knapsack[j] = max(knapsack[j], score + knapsack[j - time])

print(knapsack[t])