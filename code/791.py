class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        newstr = ""
        for c in S:
            num = T.count(c)
            newstr+=c*num
            T = T.replace(str(c),'')
        newstr+=T
        return newstr


s = Solution()
S = "cba"
T = "abcd"
print(s.customSortString(S,T))