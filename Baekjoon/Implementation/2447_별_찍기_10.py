def star(n):
    if n == 3:
        return ["***", "* *", "***"]
    
    num = n // 3
    prev = star(num)
    up_down = [prev[i] * 3 for i in range(num)]
    middle = [prev[i] + (" " * num) + prev[i] for i in range(num)]
    return up_down + middle + up_down


print(*star(int(input())), sep="\n")