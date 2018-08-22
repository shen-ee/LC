# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        newtree = TreeNode(None)
        if t1 and t2:
            newtree.val = t1.val + t2.val
            newtree.left = self.mergeTrees(t1.left,t2.left)
            newtree.right = self.mergeTrees(t1.right,t2.right)
        else:
            return t1 or t2

        return newtree

s = Solution()
