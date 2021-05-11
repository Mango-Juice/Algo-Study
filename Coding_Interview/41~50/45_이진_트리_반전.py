#이진 트리 반전
#https://leetcode.com/problems/invert-binary-tree

from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = deque([root])
        
        while queue:
            tmp = queue.popleft()
            if tmp:
                tmp.left, tmp.right = tmp.right, tmp.left
                queue.append(tmp.left)
                queue.append(tmp.right)
        
        return root
