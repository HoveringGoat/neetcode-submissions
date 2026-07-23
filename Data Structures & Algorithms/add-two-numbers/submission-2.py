# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # create a dummy node that should point to the head
        # we will return its next pointer
        fake_head = ListNode()
        last = fake_head

        remainder = 0
        # loop while we have a node value or a sum to add
        while l1 or l2 or remainder != 0:
            sum = remainder
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            # calc remainder and digit values
            digit = sum
            remainder = 0
            if sum >= 10:
                digit -= 10
                remainder = 1

            new_node = ListNode(digit, None)

            # link last node and update last node reference
            last.next = new_node
            last = new_node

        return fake_head.next
        