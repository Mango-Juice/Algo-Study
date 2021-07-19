#코스 스케줄
#https://leetcode.com/problems/course-schedule


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = {}
        
        def dfs(now: int, visited: List[int], dic_now: Dict[int, int]) -> bool:
            if now in visited:
                return False
            elif not now in dic_now.keys() or len(dic_now[now]) == 0:
                return True
            
            tmp = dic_now[now].pop()
            return dfs(tmp, visited + [now], dic_now)
        
        for a, b in prerequisites:
            if b in dic.keys():
                dic[b].append(a)
            else:
                dic[b] = [a]
        
        for key in dic.keys():
            if not dfs(key, [], dic.copy()):
                return False
            
        return True
