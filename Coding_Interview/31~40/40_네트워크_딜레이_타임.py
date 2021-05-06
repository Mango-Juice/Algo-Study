#네트워크 딜레이 타임
#https://leetcode.com/problems/network-delay-time

import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        network = {}
        distance = {}
        queue = [(0, k)]
        
        for from_, to_, time in times:
            if from_ in network.keys():
                network[from_].append((to_, time))
            else:
                network[from_] = [(to_, time)]
                
        while queue:
            time, node = heapq.heappop(queue)
            
            if not node in distance.keys():
                distance[node] = time
                if not node in network.keys():
                    continue
                for to_, ntime in network[node]:
                    heapq.heappush(queue, (time + ntime, to_))
                    
        if len(distance.keys()) == n:
            return max(distance.values())
        return -1
