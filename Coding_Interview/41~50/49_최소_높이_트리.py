#최소 높이 
#https://leetcode.com/problems/minimum-height-trees

from collections import defaultdict

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) < 1:
            return [0]
        
        dic = defaultdict(set)
        visited = set()
        answer = []
        
        for a, b in edges:
            dic[a].add(b)
            dic[b].add(a)
            
        while True:
            only_one = set()
            for key, value in dic.items():
                if not key in visited and len(value) <= 1:
                    visited.add(key)
                    only_one.add(key)
            
            if len(visited) == n:
                answer = list(only_one)
                break
                
            for key, value in dic.items():
                if not key in visited:
                    dic[key] = set.difference(dic[key], only_one)
            
        return answer
