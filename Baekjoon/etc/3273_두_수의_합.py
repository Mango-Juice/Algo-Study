#https://www.acmicpc.net/problem/3273
#https://github.com/Mango-Juice/Algo-Study/blob/main/Coding_Interview/01~10/07_두_수의_합.py 을 해결한 후 유사 문제를 풀어봄.

input()
nums = list(map(int, input().split()))
target = int(input())

answer = 0
able = set()

for num in nums:
    if num in able:
        answer += 1
    able.add(target-num)

print(answer)
