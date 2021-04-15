#홀짝 연결 리스트
#https://leetcode.com/problems/odd-even-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        
        if not head:
            return None
        
        result = odd = ListNode()
        even_result = even = ListNode()
        idx: int = 1
        
        while head:
            if(idx % 2 == 0):
                even.next = ListNode(head.val)
                even = even.next
            else:
                odd.next = ListNode(head.val)
                odd = odd.next
            head = head.next
            idx += 1
        
        odd.next = even_result.next
        return result.next
