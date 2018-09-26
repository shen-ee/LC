class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        # Solution 1
        maxlen = 0
        state = []
        llevel = 0
        for line in input.splitlines():
            isfile = line.count(".") > 0
            level = line.count("\t")
            line = line[level:]
            length = len(line)

            if level == llevel + 1:
                state.append(length)
            else:
                state[:] = state[:level]
                state.append(length)
            llevel = level

            if isfile:
                maxlen = max(maxlen,sum(state) + len(state) - 1)
        return maxlen


s = Solution()
str = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print(s.lengthLongestPath(str))