# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # Solution 1 24ms
        # if root is None:
        #     return None
        # root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        # return root

        # Solution 2 20ms
        # if not root:
        #     return None
        # root.left,root.right = self.invertTree(root.right),self.invertTree(root.left)
        # return root

        # Solution 3 20ms
        if root:
            invert = self.invertTree
            root.left,root.right = invert(root.right),invert(root.left)
        return root