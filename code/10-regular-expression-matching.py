# import re
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # # Solution 1
        # pattern = re.compile(p)
        # match = re.search(pattern,s)
        # # print(match.group())
        # return match.group() == s

        # # Solution 2
        m = len(s)
        n = len(p)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)] # dp[i][j] means isMatch(s[:i], p[:j])
        dp[0][0] = True # s[:0] = '', p[:0] = '', isMatch("","") is True
        for i in range(2,n+1): # corner case: '' can match with expressions like ''
            dp[0][i] = dp[0][i-2] and p[i-1] == '*'

        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == ".")
                else:
                    # if j-2 == -1: return False # However, I think p cannot start with '*', so this may not necessary.
                    dp[i][j] = dp[i][j-2] or ((s[i-1] == p[j-2] or p[j-2] == '.' ) and dp[i-1][j])
                    # Explanation for dp[i][j] = dp[i][j-2]:
                    #       ''(None) can match with regular expressions like '.*' or 'a*'
                    #       so if dp[i][j-2] is True, and p[j-1] is '*', then no matter p[j-2] is '.' or letter
                    # Explanation for  dp[i][j] = (s[i-1] == p[j-2] or p[j-2] == '.' ) and dp[i-1][j]:
                    #       
        return dp[m][n]

s = Solution()
print(s.isMatch('aab',"c*a*b"))
            