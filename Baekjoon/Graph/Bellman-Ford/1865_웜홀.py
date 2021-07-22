# https://www.acmicpc.net/problem/1865

import sys

input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    tree = [[] for _ in range(N + 1)]
    dist = [10 ** 9] * (N + 1)
    dist[1] = 0
    
    for _ in range(M):
        S, E, T =  map(int, input().split())
        tree[S].append((E, T))
        tree[E].append((S, T))

    for _ in range(W):
        S, E, T =  map(int, input().split())
        tree[S].append((E, -T))

    for i in range(N):
        flag = False

        for now in range(1, N + 1):
            for next_, cost in tree[now]:
                if dist[next_] > dist[now] + cost:
                    dist[next_] = dist[now] + cost
                    flag = True

        if not flag:
            break

    if flag:
        print("YES")
    else:
        print("NO")
