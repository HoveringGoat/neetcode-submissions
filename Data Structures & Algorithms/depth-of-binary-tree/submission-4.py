# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    maxDepth: int = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # gets depth of deepest node in subtree
        def maxDepth(node: Optional[TreeNode]) -> int:
            
            depth = 0
            # call recurdequesively
            queue = deque([node])
            nextQueue = deque()

            while len(queue) > 0 or len(nextQueue) > 0:
                if len(queue) == 0:
                    queue = nextQueue
                    nextQueue = deque()
                    depth += 1

                node = queue.popleft()
                if node is None:
                    continue

                nextQueue.append(node.left)
                nextQueue.append(node.right)

            return depth

        depth = maxDepth(root)
        return depth