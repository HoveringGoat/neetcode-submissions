# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        serialized = f"{self.serializeTree(root)}"
        #print(f"serialized: {serialized}")
        return serialized
        

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) ->  Optional[TreeNode]:

        # parse string back into array of int/None
        values = data[1:-1].split(",")
        array = deque([])
        for i in values:
            v = i.strip()
            if v == "None":
                array.append(None)
            else:
                array.append(int(v))

        return self.deserializeNode(array)
        
    
    def deserializeNode(self, array: deque[int]) ->  Optional[TreeNode]:
        value = array.popleft()
        if value is None:
            return None
        
        node = TreeNode(value)
        left = self.deserializeNode(array)
        right = self.deserializeNode(array)
        node.left = left
        node.right = right

        return node

    # convert a subtree into an array representation
    def serializeTree(self, node: Optional[TreeNode]) -> List[int]:
        if node is None:
            return [None]
        
        array = [node.val]
        
        left = self.serializeTree(node.left)
        right = self.serializeTree(node.right)

        array.extend(left)
        array.extend(right)

        return array




        
