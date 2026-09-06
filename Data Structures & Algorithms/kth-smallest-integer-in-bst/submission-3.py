# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        global nodes
        nodes = []

        def getSubTreeList(node: TreeNode):
            if len(nodes) >= k:
                return

            if node is None:
                return
            
            getSubTreeList(node.left)
            nodes.append(node.val)
            getSubTreeList(node.right)


        getSubTreeList(root)
        return nodes[k-1]