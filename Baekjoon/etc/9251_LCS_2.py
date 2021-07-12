#https://www.acmicpc.net/problem/9252
#최장 공통 부분 수열, 백트래킹

string1 = input()
string2 = input()

arr = [[0 for _ in range(len(string2) + 1)] for _ in range(len(string1) + 1)]

for i in range(1, len(string1) + 1):
    for j in range(1, len(string2) + 1):
        if string1[i - 1] == string2[j - 1]:
            arr[i][j] = arr[i - 1][j - 1] + 1
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

x_idx, y_idx = len(string1), len(string2)
answer = ''
print(arr[x_idx][y_idx])

while True:
    if arr[x_idx][y_idx] == 0:
        break
    
    if arr[x_idx][y_idx - 1] == arr[x_idx][y_idx]:
        y_idx -= 1
    elif arr[x_idx - 1][y_idx] == arr[x_idx][y_idx]:
        x_idx -= 1
    else:
        answer += string1[x_idx - 1]
        x_idx -= 1
        y_idx -= 1

print(answer[::-1])
