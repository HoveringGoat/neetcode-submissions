# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(node: TreeNode, min_value: int, max_value: int) -> bool:
            if not node:
                return True

            # check if we violate the min/max conditions
            if max_value is not None and node.val >= max_value:
                return False

            if min_value is not None and node.val <= min_value:
                return False
            
            # assign min/max values
            if max_value is not None:
                left_max = min(max_value, node.val)
            else:
                left_max = node.val

            # check left and right subtrees to see if they are valid too
            if not isValid(node.left, min_value, left_max):
                return False

            if min_value is not None:
                right_min = max(min_value, node.val)
            else:
                right_min = node.val
            return isValid(node.right, right_min, max_value)
            
        return isValid(root, None, None)
        