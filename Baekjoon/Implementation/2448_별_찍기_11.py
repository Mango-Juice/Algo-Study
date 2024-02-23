def star(n):
    if n == 3:
        return ["  *  ", " * * ", "*****"]
    
    num = n // 2
    prev = star(num)
    up = [(" " * num) + prev[i] + (" " * num) for i in range(num)]
    down = [prev[i] + " " + prev[i] for i in range(num)]
    return up + down


print(*star(int(input())), sep="\n")