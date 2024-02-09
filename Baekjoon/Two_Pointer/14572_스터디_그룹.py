import sys
input = sys.stdin.readline

n, k, d = map(int, input().split())
students = []

for _ in range(n):
    _, di = map(int, input().split())
    algo = list(map(int, input().split()))
    students.append((di, algo))

students.sort()
l = r = answer = 0
algos = [0] * (k + 1)
all_know = any_know = 0

for algo in students[0][1]:
    algos[algo] += 1
    all_know += 1
    any_know += 1

while True:
    cha = students[r][0] - students[l][0]
    
    if cha > d:
        for algo in range(1, k + 1):
            if algo in students[l][1]: 
                algos[algo] -= 1
                if algos[algo] == 0: any_know -= 1
            elif algos[algo] == r - l: all_know += 1
        l += 1
    else:
        answer = max(answer, (any_know - all_know) * (r - l + 1))
        r += 1
        
        if r >= n:
            break
        
        for algo in range(1, k + 1):
            if algo in students[r][1]: 
                algos[algo] += 1
                if algos[algo] == 1: any_know += 1
            elif algos[algo] == r - l: all_know -= 1

print(answer)