#조합
#https://leetcode.com/problems/combinations

from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return combinations([i + 1 for i in range(n)], k)
