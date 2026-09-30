# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    maxDepth: int = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # gets depth of deepest node in subtree
        def dfs(node: Optional[TreeNode], depth: int):
            if node is None:
                return depth

            # call recursively
            leftDepth = dfs(node.left, depth+1)
            rightDepth = dfs(node.right, depth+1)

            return max(leftDepth, rightDepth)

        depth = dfs(root, 0)
        return depth