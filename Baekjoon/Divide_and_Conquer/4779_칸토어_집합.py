import sys

def canto(n):
    if n > 0:
        return canto(n - 1) + ' ' * 3 ** (n - 1) + canto(n - 1)
    else:
        return '-'
    
datas = sys.stdin.readlines()
for data in datas:
    print(canto(int(data)))
