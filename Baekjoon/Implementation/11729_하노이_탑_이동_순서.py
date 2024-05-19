def solve(n, f, t):
    if n == 1:
        return [(f, t)]
    
    ans = []
    ans.extend(solve(n - 1, f, 6 - f - t))
    ans.append((f, t))
    ans.extend(solve(n - 1, 6 - f - t, t))
    return ans

ans = solve(int(input()), 1, 3)
print(len(ans))
for data in ans:
    print(*data)