# https://www.acmicpc.net/problem/2470

input()
liquids = sorted(map(int, input().split()))

left, right = 0, len(liquids) - 1
answer_value, answer = 2000000000, (0, 0)

while left < right:
    value = liquids[left] + liquids[right]
    if answer_value > abs(value):
        answer_value = abs(value)
        answer = (liquids[left], liquids[right])

    if answer_value == 0:
        break
    
    if value > 0:
        right -= 1
    else:
        left += 1

print("{} {}".format(*answer))
