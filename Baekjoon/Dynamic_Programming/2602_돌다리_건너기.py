target = input()
a = [input(), input()]

arr = [[[0 for _ in range(len(a[0]))] for _ in range(2)] for _ in range(len(target))]

for i in range(len(target)):
    for j in range(len(a[0])):
        for k in range(2):
            if a[k][j] == target[i]:
                if i == 0:
                    arr[i][k][j] += 1
                elif j != 0:
                    arr[i][k][j] += arr[i - 1][1 - k][j - 1]
            
            if j != 0:
                arr[i][k][j] += arr[i][k][j - 1]

print(arr[len(target) - 1][0][len(a[0]) - 1] + arr[len(target) - 1][1][len(a[0]) - 1])