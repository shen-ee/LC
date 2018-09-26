class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # Solution 1 1624ms
        # res = ""
        # flag = K
        # for c in S[::-1]:
        #     if c != '-':
        #         if flag == 0:
        #             res += '-'
        #             flag = K
        #         flag -= 1
        #         c = c.upper()
        #         res += c
        # return res[::-1]
        # Solution 2 32ms
        S = S.replace("-", "").upper()[::-1]
        res = '-'.join(S[i:i+K] for i in range(len(S))[::K])
        return res[::-1]

s = Solution()
S = "5F3Z-2e-9-w"
K = 4
print(s.licenseKeyFormatting(S,K))
