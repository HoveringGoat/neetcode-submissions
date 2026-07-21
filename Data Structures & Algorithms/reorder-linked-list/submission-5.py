# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def printList(head: Optional[ListNode]):
            current = head
            visited = set()
            i = 0
            while current:
                print(f"{i}: {current.val}")
                if current in visited:
                    print("Loop detected")
                    return
                visited.add(current)
                current = current.next
                i += 1
            return

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
        
        #printList(head)
        return

        