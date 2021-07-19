# https://www.acmicpc.net/problem/1759

from itertools import combinations

def check(chars):
    set_chars = set(chars)
    vowels = set_chars & set('aeiou')
    
    if len(vowels) == 0:
        return False
    
    set_chars -= vowels
    return len(set_chars) > 1


l, c = map(int, input().split())
alphas = sorted(input().split())

for i in list(map(''.join, list(combinations(alphas, l)))):
    if check(i):
        print(i)
