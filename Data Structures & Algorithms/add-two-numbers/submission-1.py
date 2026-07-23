# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head = None
        node = head
        last = None

        sum = 0
        # loop while we have a node value or a sum to add
        while l1 or l2 or sum != 0:
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            
            digit = sum
            if sum >= 10:
                digit -= 10
                sum -= 9

            # update sum to be either 0 if we use all the value for this digit or 1 if we carry over (sum - 9 - digit) (14 - 9 - 4 = 1)
            sum -= digit
            
            new_node = ListNode(digit, None)

            # link last node or head
            if last:
                last.next = new_node
            else:
                head = new_node

            # update last node reference
            last = new_node

        
        return head
        