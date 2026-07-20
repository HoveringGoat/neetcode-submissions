# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        # if list1.val < list2.val
        #   append list1 node to current return list and increment the list1 node along the list1 list

        head: ListNode = None
        prev: ListNode = None

        # while either list has a valid node
        while list1 or list2:
            # if list 1 is depleted attach list 2 and break
            if list1 is None:
                # trivial case where list1 was always empty
                if prev is None:
                    return list2
                prev.next = list2
                break

            # if list 2 is depleted attach list 1 and break
            elif list2 is None:
                # trivial case where list2 was always empty
                if prev is None:
                    return list1
                prev.next = list1
                break

            # normal merge
            # if list1.val is lower (or equal) add it and then move list1 up
            mergedNode: ListNode
            if list1.val <= list2.val:
                mergedNode = list1
                list1 = list1.next
            
            # same but for list2
            else:
                mergedNode = list2
                list2 = list2.next

            # we need to update the previous nodes pointer to the newly added node
            if prev:
                # if its not the first node then update prev pointer
                prev.next = mergedNode
            else:
                # if this is the first addition populate head to save start of list
                # we dont need to update previous because there is nothing pointing to this node (except head)
                head = mergedNode

            # update prev node reference
            prev = mergedNode

        return head
        