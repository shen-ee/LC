class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Solution 1 24ms
        # stack = [""]
        # for char in s:
        #     top = stack.pop()
        #     if char == ")":
        #         if top != "(":
        #             return False
        #     elif char == "]":
        #         if top != "[":
        #             return False
        #     elif char == "}":
        #         if top != "{":
        #             return False
        #     else:
        #         stack.append(top)
        #         stack.append(char)
        # return True if len(stack)==1 else False

        # Solution 2 20ms
        stack = []
        dic = {"(":")","[":"]","{":"}"}
        left = ["(","[","{"]
        for char in s:
            if char in left:
                stack.append(char)
            elif stack == []:
            # elif not stack: # what is the actual difference making this 36ms
                return False
            else:
                if char != dic[stack.pop()]:
                    return False
        return stack == []

s = Solution()
input = "{[]}"
print(s.isValid(input))
