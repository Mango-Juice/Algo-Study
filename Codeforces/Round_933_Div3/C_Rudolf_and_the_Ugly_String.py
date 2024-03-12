import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(s.count("map") + s.count("pie") - s.count("mapie"))