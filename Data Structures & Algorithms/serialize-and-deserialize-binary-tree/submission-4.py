# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        # ghetto serialization of the array
        serialized = f"{self.serializeTree(root)}"
        #print(f"serialized: {serialized}")
        return serialized
        

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) ->  Optional[TreeNode]:

        # parse string back into array of int/None
        values = data[1:-1].split(",")
        array = []
        for i in values:
            v = i.strip()
            if v == "None":
                array.append(None)
            else:
                array.append(int(v))

        return self.deserializeNode(array[::-1])
        
    # reconstructs the treenodes from the array
    # note: the array is reversed so we can pop from the end as we go
    def deserializeNode(self, reversedArray: List[int]) ->  Optional[TreeNode]:

        # remove the value from the array so subsequent calls
        # wont have the value in the array anymore.
        value = reversedArray.pop()
        if value is None:
            return None
        
        node = TreeNode(value)

        # since we remove the used values we can just pass in the array
        # and construct from what is left
        left = self.deserializeNode(reversedArray)
        right = self.deserializeNode(reversedArray)
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