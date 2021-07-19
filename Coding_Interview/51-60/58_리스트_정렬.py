#리스트 정렬
#https://leetcode.com/problems/sort-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        nodes = []
        answer = now = ListNode()
        
        while head:
            nodes.append(head.val)
            head = head.next
        
        nodes.sort()
        
        for node in nodes:
            now.next = ListNode(node)
            now = now.next
        
        return answer.next
