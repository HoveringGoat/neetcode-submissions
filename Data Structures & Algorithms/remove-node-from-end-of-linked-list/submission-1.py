# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        right = head
        left = head
        # move the right node ahead n nodes
        while n > 0:
            right = right.next
            n -= 1

        # move both nodes ahead until we reach the end.
        last = None
        while right:
            right = right.next
            last = left
            left = left.next
        
        if last:
            last.next = left.next
        else:
            head = left.next

        return head
