# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        
        head = nodes.pop(0)
        left: ListNode = head
        while len(nodes) > 0:
            # pop right
            right = nodes.pop()
            right.next = None
            left.next = right

            if len(nodes) == 0:
                break

            # pop left
            left = nodes.pop(0)
            left.next = None
            right.next = left

        