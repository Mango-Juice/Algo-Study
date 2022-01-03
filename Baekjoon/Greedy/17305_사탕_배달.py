# https://www.acmicpc.net/problem/17305

import sys
input = sys.stdin.readline

N, w = map(int, input().split())
five = []
three = []

for _ in range(N):
  t, s = map(int, input().split())
  if t == 3: three.append(s)
  else: five.append(s)

five.sort(reverse=True)
three.sort(reverse=True)

hap = []
last = 0

for i in range(min(len(five), w // 5)):
  last += five[i]
  hap.append(last)

answer = last
last = 0

for i in range(min(len(three), w // 3)):
  last += three[i]
  left_weight = (w - 3 * (i + 1)) // 5

  if hap and left_weight:
    idx = left_weight - 1 if left_weight <= len(hap) else -1
    answer = max(answer, last + hap[idx])
  else:
    answer = max(answer, last)

print(answer)
