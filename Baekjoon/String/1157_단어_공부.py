# https://www.acmicpc.net/problem/1157

from collections import Counter
common = Counter(input().upper()).most_common(2)
print(common[0][0] if len(common) < 2 else "?" if common[0][1] == common[1][1] else common[0][0])
