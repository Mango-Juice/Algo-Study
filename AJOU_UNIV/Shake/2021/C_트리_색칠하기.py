from collections import defaultdict
import sys
sys.setrecursionlimit(200001)
input = sys.stdin.readline

N = int(input())
plan = [0] + list(map(int, input().split()))
visited = [False] * (N + 1)
tree = defaultdict(list)
answer = 0


def find_answer(idx, now_color):
    global answer
    next_color = now_color
    visited[idx] = True

    if now_color != plan[idx]:
        answer += 1
        next_color = plan[idx]

    for i in tree[idx]:
        if not visited[i]:
            find_answer(i, next_color)


for _ in range(N - 1):
    i, o = map(int, input().split())
    tree[i].append(o)
    tree[o].append(i)

find_answer(1, 0)
print(answer)
