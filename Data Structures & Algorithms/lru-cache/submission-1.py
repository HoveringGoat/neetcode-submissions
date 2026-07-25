from collections import OrderedDict
class LRUCache:
    ordered: OrderedDict = OrderedDict()
    capacity: int = 0

    def __init__(self, capacity: int):
        self.ordered = OrderedDict()
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.ordered:
            self.ordered.move_to_end(key)
            return self.ordered[key]
        return -1
        

    def put(self, key: int, value: int) -> None:
        self.ordered[key] = value
        self.ordered.move_to_end(key)
        # if we're over capacity now. pop from front
        if len(self.ordered.keys()) > self.capacity:
            self.ordered.popitem(last=False)
        
