import sys
input = sys.stdin.readline

N, F, T, M = map(int, input().split())
edges = []
for _ in range(M):
    f, t, w = map(int, input().split())
    edges.append((f, t, w))

costs = list(map(int, input().split()))
new_edges = []
for f, t, w in edges:
    new_edges.append((f, t, w - costs[t]))

distances = [float("inf") for _ in range(N)]
distances[F] = -costs[F]

for i in range(N * 2):
    for f, t, w in new_edges:
        if distances[f] == float("inf"): continue
        if distances[t] > distances[f] + w:
            distances[t] = distances[f] + w
            if i >= N - 1:
                distances[t] = -float("inf")

if distances[T] == float("inf"):
    print("gg")
elif distances[T] == -float("inf"):
    print("Gee")
else:
    print(-distances[T])