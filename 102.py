# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Solution 1 32ms
        # res = []
        # if root is None:
        #     return []
        # list = [root]
        # while list:
        #     level = []
        #     list_cp = []
        #     for node in list:
        #         level.append(node.val)
        #         if node.left:
        #             list_cp.append(node.left)
        #         if node.right:
        #             list_cp.append(node.right)
        #     list = list_cp
        #     res.append(level)
        # return res
        # Solution 2 28ms
        res = []
        if root is None:
            return []
        list = [root]
        while list:
            level = []
            list_cp = []
            for node in list:
                level.append(node.val)
                if node.left is not None:
                    list_cp.append(node.left)
                if node.right is not None:
                    list_cp.append(node.right)
            list = list_cp
            res.append(level)
        return res


