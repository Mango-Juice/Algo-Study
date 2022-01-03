# https://www.acmicpc.net/problem/17300

visited = [False] * 10

L = int(input())
last = 0
answer = "YES"

for i in map(int, input().split()): 
  if visited[i]:
    answer = "NO"
    break
  
  visited[i] = True

  if last:
    # Case 1: 좌우 상황에서
    if abs(last - i) == 2 and not (i % 3 == 2 or last % 3 == 2):
      if not visited[(last + i) // 2]:
        answer = "NO"
        break

    # Case 2: 상하 상황에서
    if abs(last - i) == 6:
      if not visited[(last + i) // 2]:
        answer = "NO"
        break

    # Case 3: 대각선 상황에서
    if abs(last - i) == 8 or (min(last, i) == 3 and max(last, i) == 7):
      if not visited[(last + i) // 2]:
        answer = "NO"
        break
  
  last = i

print(answer)
