# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        head: ListNode = ListNode()
        curr: ListNode = head
        # while either list has a valid node
        while True:
            min_index = -1
            for index, node in enumerate(lists):
                if node is None:
                    continue
                if min_index == -1:
                    min_index = index
                    continue
                if node.val < lists[min_index].val:
                    min_index = index
                    continue
            
            # no value left
            if min_index == -1:
                break
            curr.next = lists[min_index]
            curr = lists[min_index]
            lists[min_index] = lists[min_index].next

        return head.next