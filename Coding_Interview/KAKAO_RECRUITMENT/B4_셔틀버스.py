#셔틀버스
#https://programmers.co.kr/learn/courses/30/lessons/17678

from collections import deque

def time_to_minute(time):
    tmp = time.split(':')
    return int(tmp[0]) * 60 + int(tmp[1])

def solution(n, t, m, timetable):
    times = deque()
    answer = 0
    
    for i in sorted(timetable):
        times.append(time_to_minute(i))
    
    for i in range(540, 540 + n * t, t):
        for _ in range(m):
                answer = times.popleft() - 1 if times and times[0] <= i else i

    h, m = answer // 60, answer % 60
    return str(h).zfill(2) + ':' + str(m).zfill(2)
