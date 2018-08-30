class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Solution 1 56ms
        # def helper(root):
        #     if not root:
        #         return 0
        #     left = helper(root.left)
        #     right = helper(root.right)
        #     if not left and right:
        #         return 1+right
        #     if left and not right:
        #         return 1+left
        #     return 1+min(left,right)
        # return helper(root)

        # Solution 2 40ms
        # if not root :
        #     return 0
        # left = self.minDepth(root.left)
        # right = self.minDepth(root.right)
        # return 1 + (min(left,right) or max(left,right))

        # Solution 3 56ms
        if not root :
            return 0
        d = map(self.minDepth,(root.left,root.right))
        return 1 + (min(d) or max(d))



