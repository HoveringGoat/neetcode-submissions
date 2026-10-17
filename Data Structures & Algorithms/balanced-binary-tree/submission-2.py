# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced: bool = True

        def getNodeMaxDepth(node: Optional[TreeNode]) -> int:
            
            nonlocal balanced

            if node is None or balanced is False:
                return 0

            leftDepth = getNodeMaxDepth(node.left)
            rightDepth = getNodeMaxDepth(node.right)
            
            diff = abs(leftDepth - rightDepth)

            if balanced == True and diff > 1:
                balanced = False
            
            depth = max(leftDepth, rightDepth) + 1
            return depth

        getNodeMaxDepth(root)
        return balanced
