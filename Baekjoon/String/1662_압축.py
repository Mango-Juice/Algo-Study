# https://www.acmicpc.net/problem/1662

from collections import deque


def solution(idx: int) -> int:
    global S, visited

    count = 0

    for i in range(idx, len(S)):
        if not visited[i]:
            if S[i] == '(':
                visited[i] = True
                count += int(S[i - 1]) * solution(i + 1) - 1

            else:
                visited[i] = True
                if S[i] == ')':
                    return count
                count += 1

    return count


S = input()
visited = [False] * len(S)

print(solution(0))
