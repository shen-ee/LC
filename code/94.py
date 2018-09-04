# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Solution 1 28ms
        # if not root : return []
        # list = []
        # inorder = self.inorderTraversal
        # if root.left:
        #     list += inorder(root.left)
        # list.append(root.val)
        # if root.right:
        #     list += inorder(root.right)
        # return list

        # Solution 2 36ms
        # if not root : return []
        # list = []
        # inorder = self.inorderTraversal
        # list += inorder(root.left)
        # list.append(root.val)
        # list += inorder(root.right)
        # return list

        # Solution 3 24ms
        list = []
        stack = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                list.append(node.val)
                root = node.right
        return list






