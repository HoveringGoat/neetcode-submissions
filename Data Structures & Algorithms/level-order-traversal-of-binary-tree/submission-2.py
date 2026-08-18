# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # the level order traversal lists
        levels: List[List[int]] = []

        # list of active nodes
        activeNodes: List[TreeNode] = []
        if root:
            activeNodes.append(root)

        # process our list of active nodes, grabbing values and 
        # child nodes which become the next set of active nodes
        while len(activeNodes) > 0:
            childNodes: List[TreeNode] = []
            depthValues = []

            for node in activeNodes:
                # first add the node value to the depth values list
                depthValues.append(node.val)

                # next add any child nodes to the child nodes list
                if node.left:
                    childNodes.append(node.left)
                if node.right:
                    childNodes.append(node.right)

            # add values to levels list
            levels.append(depthValues)

            # promote child nodes to active nodes and repeat
            activeNodes = childNodes

        return levels        