# https://www.acmicpc.net/problem/1826

##### LIBRARY IMPORT #####
import heapq


##### 주유소 정보 입력 #####
n = int(input())
gas_stations = []

for _ in range(n):
    a, b = map(int, input().split())
    heapq.heappush(gas_stations, (a, -b))


##### 마을 / 연료 정보 입력 #####
finish, fuel = map(int, input().split())
now, count = 0, 0
heap = []


##### 부릉 부릉 출발 #####
while now + fuel < finish: # 마을에 도착할 때까지 반복

    # 1. 연료가 없을 때까지 갈 수 있는 곳 탐색
    while gas_stations and gas_stations[0][0] <= now + fuel:
        pop = heapq.heappop(gas_stations)
        heapq.heappush(heap, (pop[1], pop[0]))

    # 2. 갈 수 있는 주유소가 없으면 마무리
    if not heap:
        count = -1
        break
    # 3. 갈 수 있는 주유소 중 가장 연료 많이 주는 곳 들르자!
    else:
        pop = heapq.heappop(heap)
        fuel -= pop[1] - now + pop[0]
        now = pop[1]
        count += 1


##### 결과 출력 #####
print(count)
