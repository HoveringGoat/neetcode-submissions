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
            global currMax
            
            # sum is the current incoming "value" of connecting upstream.
            # we can only make ONE connection. upstream to left or right
            # or left and right together.

            # all routes will go through our node value. so we can ignore that for now.
            
            

            #print(f"node: {node.val}, sum: {sum}")

            sumLeft = findPaths(node.left, sum + node.val)
            sumRight = findPaths(node.right, sum + node.val)

            # connect upstream + max downstream
            maxSumChild = max(sumRight, sumLeft)
            maxSumChild = max(maxSumChild, 0)
            newMax = maxSumChild + sum + node.val

            #print(f"node: {node.val}, sum: {sum}, max: {newMax}, sumLeft: {sumLeft}, sumRight: {sumRight}")

            # connect left + right
            newSum = sumLeft + sumRight + node.val

            # record the sum from connecting left + right
            if newSum > newMax and newSum > self.currMax:
                self.currMax = newSum
            
            # record max starting from here.
            if maxSumChild + node.val > self.currMax:
                self.currMax = maxSumChild + node.val

            # return the value of the downsteam sum. 
            return maxSumChild + node.val

        self.currMax = root.val
        maxSum = findPaths(root, 0)

        return max(maxSum, self.currMax)


        