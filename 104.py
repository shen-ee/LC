from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Solution 1 68ms
        # if not root:
        #     return 0
        # else:
        #     return max(self.maxDepth(root.left),self.maxDepth(root.right))+1

        # Solution 2 40ms
        # if root is None:
        #     return 0
        # else:
        #     return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # Solution 3 36ms
        # if root is None:
        #     return 0
        # return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # Solution 4 36ms
        # if root is None:
        #     return 0
        # depth = 1
        # tmp = [[1,root]]
        # while tmp:
        #     depth,node = tmp.pop(0)
        #     if node.left:
        #         tmp.append([depth+1,node.left])
        #     if node.right:
        #         tmp.append([depth+1,node.right])
        # return depth

        # Solution 5 32ms
        # if not root :
        #     return 0
        # depth = 1
        # tmp = [[1,root]]
        # while tmp:
        #     depth,node = tmp.pop(0)
        #     if node.left:
        #         tmp.append([depth+1,node.left])
        #     if node.right:
        #         tmp.append([depth+1,node.right])
        # return depth

        # Solution 6 32ms
        if not root:
            return 0
        depth = 1
        queue = deque([(1,root)])
        while queue:
            depth,node = queue.popleft()
            if node.left:
                queue.append((depth+1,node.left))
            if node.right:
                queue.append((depth+1,node.right))
        return depth