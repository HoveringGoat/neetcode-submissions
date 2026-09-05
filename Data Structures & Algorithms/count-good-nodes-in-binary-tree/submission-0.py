# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        
        def processNodes(node: TreeNode, largestValue: int) -> int:
            if not node:
                return 0

            goodNodes: int = 0
            # good value - increment and update largest value
            if largestValue is None or node.val >= largestValue:
                largestValue = node.val
                goodNodes += 1
            
            # left
            leftLargest = largestValue
            leftGoodNodes = processNodes(node.left, leftLargest)

            # right
            rightLargest = largestValue
            rightGoodNodes = processNodes(node.right, rightLargest)

            return goodNodes + leftGoodNodes + rightGoodNodes
        
        good = processNodes(root, None)

        return good