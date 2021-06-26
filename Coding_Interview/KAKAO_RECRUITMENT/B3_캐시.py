#캐시
#https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    
    answer = 0
    cache = deque()
    
    for i in cities:
        city = i.lower()
        
        if city in cache:
            cache.remove(city)
            answer += 1
        else:
            if len(cache) == cacheSize:
                cache.popleft()
            answer += 5
            
        cache.append(city)
        
    return answer
