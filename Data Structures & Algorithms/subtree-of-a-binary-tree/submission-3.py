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
        
        isContained: bool = False

        def dfs(node: Optional[TreeNode]):
            # traverse tree until node val == subtree value.
            # if we are equal check if subtree is equal
            # if it is abort out and return tree.
            # if not continue search until we exhaust tree
            nonlocal isContained

            if node is None or isContained:
                return

            # check subtree
            if node.val == subRoot.val:
                if isSameTree(node, subRoot):
                    isContained = True
                    return
                
            dfs(node.left)
            dfs(node.right)
            return
        
        dfs(root)
        return isContained
            
            


        