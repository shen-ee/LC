# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # Solution 1 44ms
        # res = []
        # if root is None:
        #     return []
        # list = [root]
        # flag = False
        # while list:
        #     level = []
        #     list_cp = []
        #     for node in list:
        #         level.append(node.val)
        #         if node.left is not None:
        #             list_cp.append(node.left)
        #         if node.right is not None:
        #             list_cp.append(node.right)
        #     list = list_cp
        #     if flag:
        #         level.reverse()
        #         flag = False
        #     else:
        #         flag = True
        #     res.append(level)
        # return res

        # Solution 2 24ms
        if root is None: return []
        res,list,flag = [],[root],-1
        while list:
            level = []
            for i in range(0,len(list)):
                node = list.pop(0)
                level.append(node.val)
                if node.left is not None:
                    list.append(node.left)
                if node.right is not None:
                    list.append(node.right)
            res.append(level[::flag])
            flag *= -1
        return res



