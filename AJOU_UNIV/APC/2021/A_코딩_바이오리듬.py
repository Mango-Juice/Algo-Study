# A

import sys
input = sys.stdin.readline

target = input()

def get_bio(date):
    result = tmp = 0
    
    for i in range(4):
        result += (int(date[i]) - int(target[i])) ** 2

    for i in range(4, 6):
        tmp += (int(date[i]) - int(target[i])) ** 2

    result *= tmp
    tmp = 0

    for i in range(6, 8):
        tmp += (int(date[i]) - int(target[i])) ** 2

    result *= tmp
    return result

n = int(input())
max_idx, max_val = "", -1

for _ in range(n):
    tmp = input().rstrip()
    val = get_bio(tmp)

    if val > max_val or (val == max_val and max_idx > tmp):
        max_idx, max_val = tmp, val

print(max_idx)
