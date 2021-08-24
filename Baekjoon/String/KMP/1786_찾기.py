# https://www.acmicpc.net/problem/1786

def init():  # pi 배열 만들기 (전처리)
    global T, P, arr

    j = 0
    for i in range(1, len(P)):
        while j > 0 and P[i] != P[j]:
            j = arr[j - 1]

        if P[i] == P[j]:
            j += 1
            arr[i] = j


def kmp():  # 탐색
    global T, P, arr

    j = 0
    for i in range(len(T)):
        while j > 0 and T[i] != P[j]:
            j = arr[j - 1]

        if T[i] == P[j]:
            if j == len(P) - 1:
                answer.append(i - len(P) + 2)
                j = arr[j]
            else:
                j += 1


T = input()
P = input()

arr = [0] * len(P)
answer = []

init()
print(arr)
kmp()

print(len(answer))
print(*answer)
