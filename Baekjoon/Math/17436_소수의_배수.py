answer = 0

def solve(index, number, count):
    global answer
    if count & 1:
        answer += m // (number * arr[index])
    else:
        answer -= m // (number * arr[index])

    if index < n - 1:
        solve(index + 1, number * arr[index], count + 1)
        solve(index + 1, number, count)


n, m = map(int, input().split())
arr = list(map(int, input().split()))

solve(0, 1, 1)
print(answer)