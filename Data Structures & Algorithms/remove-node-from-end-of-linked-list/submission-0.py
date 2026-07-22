# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        stack = []
        curr = head

        # Populate Stack With All The List Nodes 
        while curr:
            stack.append(curr)
            curr = curr.next

        # trivial case of popping first node
        if len(stack) == n:
            return head.next

        popped: ListNode = None

        # Pop N Nodes Off The Stack
        for i in range(n):
            popped = stack.pop() 
        
        # Set The Nth + 1 To Last Nodes Next Pointer To The Nth-1 Node
        stack.pop().next = popped.next

        return head
