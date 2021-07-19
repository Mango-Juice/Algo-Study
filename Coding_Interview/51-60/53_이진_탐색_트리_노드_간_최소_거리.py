#이진 탐색 트리 노드 간 최소 거리
#https://leetcode.com/problems/minimum-distance-between-bst-nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    answer = 100000
    tmp = -10000
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)
            
        self.answer, self.tmp = min(self.answer, root.val - self.tmp), root.val
        
        if root.right:
            self.minDiffInBST(root.right)
            
        return self.answer
