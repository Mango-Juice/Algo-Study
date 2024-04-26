import sys, datetime
from collections import defaultdict
input = sys.stdin.readline

n, l, f = input().split()
n, f = int(n), int(f)

l_day, l_hour_minute = l.split('/')
l_hour, l_minute = l_hour_minute.split(':')
l_delta = datetime.timedelta(days=int(l_day), hours=int(l_hour), minutes=int(l_minute))

status = defaultdict(dict)
answer = defaultdict(int)
for _ in range(n):
    date, time, thing, name = input().split()
    dt = datetime.datetime.strptime(date + ' ' + time, '%Y-%m-%d %H:%M')
    
    if name in status[thing]:
        delta = dt - status[thing][name]
        if delta > l_delta:
            answer[name] += int((delta - l_delta).total_seconds() // 60 * f)
        del status[thing][name]
    else:
        status[thing][name] = dt

if not answer: print(-1)
for key in sorted(answer.keys()):
    print(key, answer[key])