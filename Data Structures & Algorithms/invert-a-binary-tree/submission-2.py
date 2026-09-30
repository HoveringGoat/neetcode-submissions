# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverseNodes(node: Optional[TreeNode]):
            if node is None:
                return

            # save refs
            left = node.left
            right = node.right

            # reverse
            node.left = right
            node.right = left

            # reverse children recursively
            reverseNodes(left)
            reverseNodes(right)

        reverseNodes(root)
        return root