#역순 연결 리스트
#https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right or not head:
            return head
        
        result = head = ListNode(0, head)
        
        for _ in range(left-1):
            head = head.next
        end = head.next
            
        for _ in range(right - left):
            tmp, head.next, end.next = head.next, end.next, end.next.next
            head.next.next = tmp
            
        return result.next
