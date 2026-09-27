# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Range:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end
        self.length = end - start + 1

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # generate inordermap
        inorderMap = {}
        for index, value in enumerate(inorder):
            inorderMap[value] = index

        # generate preordermap
        preorderMap = {}
        for index, value in enumerate(preorder):
            preorderMap[value] = index

        # print(f"inorder: {inorderMap}")
        # print(f"preorder: {preorderMap}")

        def getLeftInorderRange(rootInorderIndex: int, inorderRange: Range) -> Range:
            end = rootInorderIndex - 1
            leftInorderRange = Range(inorderRange.start, end)
            return leftInorderRange


        def getRightInorderRange(rootInorderIndex: int, inorderRange: Range) -> Range:
            start = rootInorderIndex + 1
            rightInorderRange = Range(start, inorderRange.end)
            return rightInorderRange


        def getLeftPreorderRange(leftInorderRange: Range, preOrderRange: Range) -> Range:
            start = preOrderRange.start + 1
            end = start + leftInorderRange.length - 1
            leftPreorderRange = Range(start, end)
            return leftPreorderRange


        def getRightPreorderRange(leftPreorderRange: Range, preOrderRange: Range) -> Range:
            start = leftPreorderRange.end + 1
            rightPreorderRange = Range(start, preOrderRange.end)
            return rightPreorderRange


        def buildSubTree(preorderRange: Range, inorderRange: Range) -> Optional[TreeNode]:
            # trivial case None node
            if preorderRange.length == 0:
                return None

            node = TreeNode(preorder[preorderRange.start])

            # trivial case single length
            if preorderRange.length == 1:
                return node

            #print(f"preorder: {preorder[preorderRange.start:preorderRange.end + 1]}, inorder: {inorder[inorderRange.start:inorderRange.end+1]}, node: {node.val}")


            # calc left subtree length
            # calc right subtree length
            
            # call helper method to calc pre/inorder ranges for
            # right and left subtree based on length

            inorderNodeIndex = inorderMap[node.val]

            leftInorderRange = getLeftInorderRange(inorderNodeIndex, inorderRange)
            leftPreorderRange = getLeftPreorderRange(leftInorderRange, preorderRange)

            #print(f"left subtree: prerange: {preorder[leftPreorderRange.start:leftPreorderRange.end + 1]}, inorderRange: {inorder[leftInorderRange.start:leftInorderRange.end+1]}")

            rightInorderRange = getRightInorderRange(inorderNodeIndex, inorderRange)
            rightPreorderRange = getRightPreorderRange(leftPreorderRange, preorderRange)


            #print(f"right subtree: prerange: {preorder[rightPreorderRange.start:rightPreorderRange.end + 1]}, inorderRange: {inorder[rightInorderRange.start:rightInorderRange.end+1]}")

            left = buildSubTree(leftPreorderRange, leftInorderRange)
            right = buildSubTree(rightPreorderRange, rightInorderRange)

            node.left = left
            node.right = right
            return node

        preorderRange = Range(0, len(preorder)-1)
        inorderRange = Range(0, len(inorder)-1)
        root = buildSubTree(preorderRange, inorderRange)

        return root
        