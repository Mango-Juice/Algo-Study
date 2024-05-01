import sys
input = sys.stdin.readline

n = int(input())

if n > 1023:
    print(-1)
    exit()

for a in range(10):
    for b in range(10):
        if a <= b and not a == 0: continue
        for c in range(10):
            if b <= c and not a == b == 0: continue
            for d in range(10):
                if c <= d and not a == b == c == 0: continue
                for e in range(10):
                    if d <= e and not a == b == c == d == 0: continue
                    for f in range(10):
                        if e <= f and not a == b == c == d == e == 0: continue
                        for g in range(10):
                            if f <= g and not a == b == c == d == e == f == 0: continue
                            for h in range(10):
                                if g <= h and not a == b == c == d == e == f == g == 0: continue
                                for i in range(10):
                                    if h <= i and not a == b == c == d == e == f == g == h == 0: continue
                                    for j in range(10):
                                        if i <= j and not a == b == c == d == e == f == g == h == i == 0: continue
                                        n -= 1
                                        if n == 0:
                                            print(int(f"{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}"))
                                            exit(0)