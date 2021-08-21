# https://www.acmicpc.net/problem/12438

import sys
input = sys.stdin.readline

for i in range(1, int(input()) + 1):
    cycle = r = c = 0
    MONTH_COUNT, DAY_PER_MONTH, DAY_PER_WEEK = map(int, input().split())
    answer = (MONTH_COUNT * DAY_PER_MONTH) // DAY_PER_WEEK

    if DAY_PER_MONTH % DAY_PER_WEEK != 0:
        while c != DAY_PER_WEEK:
            if DAY_PER_WEEK > c > 0: r += 1

            r += DAY_PER_MONTH // DAY_PER_WEEK
            c += DAY_PER_MONTH % DAY_PER_WEEK

            if c > DAY_PER_WEEK:
                r += 1
                c -= DAY_PER_WEEK

            cycle += 1
            
        answer += MONTH_COUNT - (MONTH_COUNT // cycle)

    print(f"Case #{i}: {answer}")
