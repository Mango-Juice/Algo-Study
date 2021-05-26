#구간 병합
#https://leetcode.com/problems/merge-intervals

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x : x[0])
        answer = []
        now = sorted_intervals[0]
        
        for i in sorted_intervals[1:]:
            if now[1] < i[0]:
                answer.append(now)
                now = i
            else:
                now[1] = max(now[1], i[1])
        
        answer.append(now)
        return answer
