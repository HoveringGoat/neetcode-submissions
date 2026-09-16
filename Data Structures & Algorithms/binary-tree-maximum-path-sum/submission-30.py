# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    currMax: int
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def findPaths(node: TreeNode, sum: int) -> int:

            if node is None:
                return 0
            
            # sum is the current summed value from upstream.
            # we can only make ONE connection. upstream to left or right
            # or left and right together.
            # OR just this subtree down (through one of the child nodes)

            # these will get the value of the subtree sums
            # they will NOT include the upstream sum as part of the returned value
            # upstream sum is passed in for max sum calculations
            sumLeft = findPaths(node.left, sum + node.val)
            sumRight = findPaths(node.right, sum + node.val)

            # connect upstream + max downstream
            maxSumChild = max(sumRight, sumLeft)

            # if both child sums are negative no point including them
            maxSumChild = max(maxSumChild, 0)
            newMax = maxSumChild + sum + node.val

            # connect left + right
            newSum = sumLeft + sumRight + node.val

            # record the sum from connecting left + right
            if newSum > newMax and newSum > self.currMax:
                self.currMax = newSum
            
            # record max starting from here
            # (not including upstream and not including one of the child nodes)
            if maxSumChild + node.val > self.currMax:
                self.currMax = maxSumChild + node.val

            # return the value of the downsteam sum + current node value
            return maxSumChild + node.val

        # init max to first root value
        self.currMax = root.val
        maxSum = findPaths(root, 0)

        # max is either the largest straight line path value (max sum)
        # or some subtree connected graph (should be in currMax)
        return max(maxSum, self.currMax)


        