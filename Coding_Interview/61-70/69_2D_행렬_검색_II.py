#2D 행렬 검색
#https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        
        y, x = 0, len(matrix[0]) - 1
        
        while y < len(matrix) and x >= 0:
            value = matrix[y][x]
            if value == target:
                return True
            elif value > target:
                x -= 1
            elif value < target:
                y += 1
            
        return False
