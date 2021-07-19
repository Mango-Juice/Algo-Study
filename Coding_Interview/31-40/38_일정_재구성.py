#일정 재구성
#https://leetcode.com/problems/reconstruct-itinerary

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        journey = {}
        answer = []
        
        for i in sorted(tickets, key = lambda x : x[1], reverse = True):
            if i[0] in journey.keys():
                journey[i[0]].append(i[1])
            else:
                journey[i[0]] = [i[1]]
        
        def dfs(place: str) -> None:
            while place in journey.keys() and journey[place]:
                dfs(journey[place].pop())
            answer.append(place)
        
        dfs("JFK")
        
        return answer[::-1]
