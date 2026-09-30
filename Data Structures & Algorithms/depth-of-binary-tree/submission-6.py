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
        def maxDepth(node: Optional[TreeNode]) -> int:
            
            depth = 0
            childNodes: List[TreeNode] = [node]

            while len(childNodes) > 0:
                nodes: List[TreeNode] = childNodes[:]
                childNodes = []

                for node in nodes:
                    if node is None:
                        continue
                    childNodes.append(node.left)
                    childNodes.append(node.right)

                depth += 1

            return depth - 1

        depth = maxDepth(root)
        return depth