# https://www.acmicpc.net/problem/4354

def pi(s, n):
    j = 0
    result = [0] * n

    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = result[j - 1]

        if s[i] == s[j]:
            j += 1
            result[i] = j

    return result


while True:
    s = input()
    n = len(s)

    if s == '.':
        break

    arr = pi(s, n)

    if arr[-1] == 0 or arr[-1] % (n - arr[-1]) != 0:
        print(1)
    else:
        print(n // (n - arr[-1]))
