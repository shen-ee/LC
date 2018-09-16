# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def helper(node):
            if node :
                vals.append(node.val)
                helper(node.left)
                helper(node.right)
            else:
                vals.append(None)
        vals = []
        helper(root)
        return vals

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def helper():
            val = next(vals)
            if val == None:
                return None
            node = TreeNode(val)
            node.left = helper()
            node.right = helper()
            return node

        vals = iter(data)
        return helper()



        # Your Codec object will be instantiated and called as such:
codec = Codec()
# codec.deserialize(codec.serialize(root))
