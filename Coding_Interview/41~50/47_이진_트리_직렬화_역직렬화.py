#이진 트리 직렬화 & 역직렬화
#https://leetcode.com/problems/serialize-and-deserialize-binary-tree

from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root) -> List:
        queue = deque([root])
        answer = []
        
        while queue:
            now = queue.popleft()
            if now:
                queue.append(now.left)
                queue.append(now.right)
                answer.append(now.val)
            else:
                answer.append(None)
                
        return answer
        
        
    def deserialize(self, data) -> TreeNode:
        if data[0] == None:
            return None

        root = TreeNode(data[0])
        queue = deque([root])
        idx = 1;
        
        while queue:
            now = queue.popleft()
            if data[idx] != None:
                now.left = TreeNode(int(data[idx]))
                queue.append(now.left)
            idx += 1
            
            if data[idx] != None:
                now.right = TreeNode(int(data[idx]))
                queue.append(now.right)
            idx += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
