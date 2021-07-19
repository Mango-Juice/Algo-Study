#삽입 정렬 리스트
#https://leetcode.com/problems/insertion-sort-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        answer = now = ListNode(-5000)
        
        while head:
            if now.val > head.val:
                now = answer
                
            while now.next and now.next.val < head.val:
                now = now.next
            
            now.next, head.next, head = head, now.next, head.next
        
        return answer.next
