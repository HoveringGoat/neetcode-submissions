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

        # if we're already at the end then we need to remove the first node - just update head
        if not right:
            head = head.next
            return head
        
        # move both nodes ahead until we reach the end.
        last = None
        while right:
            right = right.next
            last = left
            left = left.next
        
        # update last node next pointer to removed node's next pointer
        last.next = left.next

        return head
