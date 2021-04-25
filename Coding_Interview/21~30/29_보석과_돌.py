#보석과 돌
#https://leetcode.com/problems/jewels-and-stones

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([i in jewels for i in stones])
