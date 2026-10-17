# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(nodeA: Optional[TreeNode], nodeB: Optional[TreeNode]) -> bool:
            # ensure that nodes exist
            if nodeA is None and nodeB is None:
                return True
            if nodeA is None or nodeB is None:
                return False
            
            # ensure values are equal
            if nodeA.val != nodeB.val:
                return False

            # traverse left subtree
            if isSameTree(nodeA.left, nodeB.left) == False:
                return False
            
            # traverse right subtree
            return isSameTree(nodeA.right, nodeB.right)
        
            dfs(node.left)
            dfs(node.right)
            return
        
        if isSameTree(root, subRoot):
            return True
        
        if root is None:
            return False
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
