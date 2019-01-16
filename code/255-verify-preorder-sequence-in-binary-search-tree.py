class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if preorder == []:
            return False
        stack = []
        root = preorder[0]
        for i in preorder[1:]:
            top = stack[-1]
            if i < top:
                stack.append[i]
            else:
                if stack!=[]:
                    stack.pop()          
        if len(stack) != 1:
            return False
        return True

