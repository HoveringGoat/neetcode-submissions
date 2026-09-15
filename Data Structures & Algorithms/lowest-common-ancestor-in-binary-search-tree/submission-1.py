# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        current: TreeNode = root

        while current is not None:

            # check if target node values are all greater or all lesser than current nodes value
            # (all on one side of the current tree)
            allGreater: bool = p.val > current.val and q.val > current.val
            allLesser: bool = p.val < current.val and q.val < current.val

            # if they are adjust current node and continue
            if allGreater:
                current = current.right
                continue
            
            if allLesser:
                current = current.left
                continue

            # if they are not, current node is the LCA
            break

        return current        