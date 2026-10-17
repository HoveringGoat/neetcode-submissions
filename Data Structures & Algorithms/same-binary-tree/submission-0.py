# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def traverseBothTrees(nodeA: Optional[TreeNode], nodeB: Optional[TreeNode]) -> bool:
            # ensure that nodes exist
            if nodeA is None and nodeB is None:
                return True
            if nodeA is None or nodeB is None:
                return False
            
            # ensure values are equal
            if nodeA.val != nodeB.val:
                return False

            # traverse left subtree
            if traverseBothTrees(nodeA.left, nodeB.left) == False:
                return False
            return traverseBothTrees(nodeA.right, nodeB.right)
        return traverseBothTrees(p, q)
