# Next Permutation

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    word = list(input().rstrip())
    chars = sorted(word)
    orders = [chars.index(i) for i in word]
    
    for i in range(len(word) - 1, -1, -1):
        if orders[i] > orders[i - 1]:
            break

    if i == 0:
        print(''.join(word))
        continue
    
    for j in range(len(word) - 1, i - 1, -1):
        if orders[j] > orders[i - 1]:
            orders[j], orders[i - 1] = orders[i - 1], orders[j]
            break
    
    orders = orders[:i] + orders[:i-1:-1]
    
    print(''.join([chars[i] for i in orders]))
