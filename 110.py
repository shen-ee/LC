class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root):
            if not root:
                return 0
            left = check(root.left)
            right = check(root.right)
            if abs(left - right) > 1 or left == -1 or right == -1 :
                return -1
            return 1 + max(left, right)
        if check(root)==-1:
            return False
        return True

