class Node:
    prev: Node = None
    next: Node = None
    val: int
    key: int

    def __init__(self, k:int, v:int):
        self.key = k
        self.val = v

class LRUCache:
    capacity: int = 0
    head: Node = None
    tail: Node = None
    nodes: dict[int, Node]

    def __init__(self, capacity: int):
        # init the values
        self.capacity = capacity
        self.nodes = {}
        

    def get(self, key: int) -> int:
        # if we have key. move to end and return the value
        if key in self.nodes:
            self.move_to_end(self.nodes[key])
            return self.nodes[key].val
        
        # we aint got it
        return -1
        

    def put(self, key: int, value: int) -> None:

        # key exists - update
        if key in self.nodes:
            self.move_to_end(self.nodes[key])
            self.nodes[key].val = value
            #self.printlist()
            return
        
        # new key - add node
        new_node = Node(key, value)
        self.nodes[key] = new_node
        if self.head is None:
            self.tail = new_node
            self.head = new_node
        else:
            self.append_to_tail(new_node)
        

        # if we're over capacity now. pop from front
        if len(self.nodes.keys()) > self.capacity:
            self.remove_least()

        
    def move_to_end(self, node: Node):
        if node.next is None:
            return
        # disconnect the node
        if node.prev is None or node == self.head:
            self.head = node.next
            node.next.prev = node.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        
        self.append_to_tail(node)


    def append_to_tail(self, node: Node):
        self.tail.next = node
        node.prev = self.tail
        node.next = None
        self.tail = node
        return


    def remove_least(self):
        self.nodes.pop(self.head.key)
        self.head = self.head.next


    def printlist(self):
        curr = self.head
        print("node list")
        i = 0
        while curr:
            print(f"{i} = {curr.key}:{curr.val}")
            if curr == curr.next:
                print("abort! loop detected.")
                break
            curr = curr.next
            i += 1
    


