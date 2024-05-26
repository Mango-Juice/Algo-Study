def solve(nn, nr, nc):
    if nn == 0: return 0
    
    half_size = 2 ** (nn - 1)
    pre = 0
    if nr >= half_size: pre += 2 ** (2 * nn - 1)
    if nc >= half_size: pre += 2 ** (2 * nn - 2)
    return pre + solve(nn - 1, nr % half_size, nc % half_size)


n, r, c = map(int, input().split())
print(solve(n, r, c))