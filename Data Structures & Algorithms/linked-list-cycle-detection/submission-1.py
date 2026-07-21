# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        current = head
        visited = set()

        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next
        return False
        