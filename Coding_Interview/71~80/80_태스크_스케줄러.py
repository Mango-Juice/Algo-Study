#태스크 스케줄러
#https://leetcode.com/problems/task-scheduler

from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        answer = 0
        counter = Counter(tasks)
        
        while True:
            sub_count = 0
            
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                answer += 1
                counter.subtract(task)
                counter += Counter() #음수 아이템 제거
            
            if not counter:
                break
            
            answer += n - sub_count + 1 #idle 횟수
        
        return answer
