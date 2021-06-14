#키에 따른 대기열 재구성
#https://leetcode.com/problems/queue-reconstruction-by-height

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people_sorted = sorted([(x, -y) for x, y in people], reverse = True)
        answer = []
        for height, order in people_sorted:
            answer.insert(-order, [height, -order])
        return answer
