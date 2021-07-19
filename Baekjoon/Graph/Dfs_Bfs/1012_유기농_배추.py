# https://www.acmicpc.net/problem/1012

from collections import deque

direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
testcases = int(input())
        
for _ in range(testcases):
    width, length, count = map(int, input().split())
    baechoo = deque()
    answer = 0
    
    for _ in range(count):
        baechoo.append(tuple(map(int, input().split())))

    while baechoo:
        answer += 1
        queue = deque([baechoo.popleft()])

        while queue:
            now = queue.popleft()
            for x, y in direction:
                tmp = (now[0] + x, now[1] + y)
                if tmp in baechoo:
                    baechoo.remove(tmp)
                    queue.append(tmp)

    print(answer)
