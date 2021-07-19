# https://www.acmicpc.net/problem/2696
# heap

##### 라이브러리 import #####
import heapq

##### 테스트케이스 수 입력 #####
t = int(input())

########## 메인 ##########
for _ in range(t):
    
    # 수열 입력
    n = int(input())
    nums = list(map(int, input().split()))

    while n > 10:
        n -= 10
        nums.extend(list(map(int, input().split())))

    # 필요한 변수 선언
    answer = [nums[0]]
    max_heap = []
    min_heap = []
    pivot = nums[0]

    # 힙을 이용해 answer에 중앙값 append
    for idx, data in enumerate(nums[1:]):
        if data < pivot: # pivot보다 작으면 최대 힙에 push
            heapq.heappush(max_heap, -data)
        else: # pivot보다 크면 최소 힙에 push
            heapq.heappush(min_heap, data)

        if idx % 2 == 1: #홀수 번째 수라면
            if len(max_heap) > len(min_heap): # 최대 힙의 원소 수가 많으면
                heapq.heappush(min_heap, pivot) # 최소 힙에 피봇 추가
                pivot = -heapq.heappop(max_heap) # 새로운 피봇은 최대 힙에서 pop
            elif len(max_heap) < len(min_heap): # 최소 힙의 원소 수가 많으면
                heapq.heappush(max_heap, -pivot) # 최대 힙에 피봇 추가
                pivot = heapq.heappop(min_heap) # 새로운 피봇은 최소 힙에서 pop

            answer.append(pivot) # 중앙값은 pivot

    # 수열 출력
    idx = 0
    length = len(answer)
    print(length)

    while idx < length:
        print(' '.join(map(str, answer[idx:min(idx + 10, length)])))
        idx += 10
