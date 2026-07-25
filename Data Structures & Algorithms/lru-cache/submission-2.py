from collections import OrderedDict
class LRUCache:
    ordered: OrderedDict = OrderedDict()
    capacity: int = 0

    def __init__(self, capacity: int):
        # init the values
        self.ordered = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        # if we have key. move to end and return the value
        if key in self.ordered:
            self.ordered.move_to_end(key)
            return self.ordered[key]
        
        # we aint got it
        return -1
        

    def put(self, key: int, value: int) -> None:
        # add or update value
        self.ordered[key] = value

        # move this node to the end (we might not have added and just updated it)
        self.ordered.move_to_end(key)

        # if we're over capacity now. pop from front
        if len(self.ordered.keys()) > self.capacity:
            self.ordered.popitem(last=False)
        
