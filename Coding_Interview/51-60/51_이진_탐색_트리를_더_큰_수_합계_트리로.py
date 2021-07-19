#이진 탐색 트리를 더 큰 수 합계 트리로
#https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    val: int = 0
        
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right) #오른쪽꺼 탐색해서
            self.val += root.val #값에 더한다
            root.val = self.val #그 값이 바로 현재 노드의 값
            self.bstToGst(root.left) #이제 왼쪽꺼 탐색해야징
            
        return root
