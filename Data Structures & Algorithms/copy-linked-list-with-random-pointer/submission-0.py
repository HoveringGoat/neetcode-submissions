"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # create list of mapped random indicies [none, 3, 0, 1]
        # create dict of new nodes
        # walk through and create nodes in new list
        # when we go to create a node check if it already was created in the dict
        # if it is go ahead and update the value and pointers
        # try to populate random first.
        # if possible connect it with an existing node. if node isnt created yet create and 
        # add to dict with the index as the key

        # we need a dict of og nodes first
        curr = head
        index = 0

        # node is key, index is value
        mapped = {}
        while curr:
            mapped[curr] = index
            curr = curr.next
            index += 1
        
        curr = head
        # index is key, node is value
        nodes = {}
        copy_head = Node(0)
        copy = copy_head
        index = 0
        while curr:
            new_node: Node
            if index in nodes:
                new_node = nodes[index]
            else:
                new_node = Node(curr.val)
                nodes[index] = new_node

            # set random node pointer
            if curr.random != None:
                # random is a node
                random_index = mapped[curr.random]
                if random_index in nodes:
                    # random node exists
                    new_node.random = nodes[random_index]
                else:
                    # random node does not exist
                    new_random_node = Node(curr.random.val)

                    nodes[random_index] = new_random_node
                    new_node.random = new_random_node

            else:
                # no random node
                new_node.random = None

            copy.next = new_node
            copy = new_node
            curr = curr.next
            index += 1

        return copy_head.next
        