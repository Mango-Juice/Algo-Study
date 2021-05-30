#원점에서 K번째로 가까운 점
#https://leetcode.com/problems/k-closest-points-to-origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key = lambda x : x[0] ** 2 + x[1] ** 2)[:k]
