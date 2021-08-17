# https://www.acmicpc.net/problem/12849

MOD = 1000000007
MAP = { 0 : [1, 2],
        1 : [0, 2, 4],
        2 : [0, 1, 4, 3],
        3 : [2, 4, 5, 7],
        4 : [1, 2, 3, 5],
        5 : [4, 3, 6],
        6 : [5, 7],
        7 : [3, 6] }
arr = [int(i == 0) for i in range(8)]

def solution():
    global MAP, arr
    new_arr = []

    for i in range(8):
        tmp = 0
        for j in MAP[i]: tmp += arr[j]
        new_arr.append(tmp % MOD)

    arr = new_arr

for _ in range(int(input())): solution()

print(arr[0])
