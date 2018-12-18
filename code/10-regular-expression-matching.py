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
        dp = [[False for i in range(n+1)] for j in range(m+1)] # dp[i][j] stores the result of isMatch(s[:i], p[:j])
        dp[0][0] = True # s[:0] = '', p[:0] = '', isMatch("","") is True
        for i in range(2,n+1): # corner case: '' can match with expressions like 'a*b*c*.*'
            dp[0][i] = dp[0][i-2] and p[i-1] == '*'

        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (s[i-1] == p[j-1] or p[j-1] == ".")
                    '''
                    Explanation:
                        Reguar single step check, for example:
                            In a case, p[j-1] = 'a', s[:i] = 'bua', p[:j] = 'bua':
                            In order to check if 'bua' matches 'bua',
                            we have to check if (('bu' matches 'bu') and ('a' matches 'a'))
                    '''   
                else: # current pattern p[j-1] is '*', we need to know the preceding element p[j-2]
                    # if j-2 == -1: return False # However, I think p cannot start with '*', so this may not necessary.
                    dp[i][j] = dp[i][j-2] or ((s[i-1] == p[j-2] or p[j-2] == '.' ) and dp[i-1][j])
                    '''
                    We have two possibilites:
                        1. s[:i] does not end with p[j-2](the preceding element)  --> dp[i][j-2]
                        2. s[:i] ends with p[j-2](the preceding element) --> (s[i-1] == p[j-2] or p[j-2] == '.' ) and dp[i-1][j]

                    Explanation for alternative1 dp[i][j] = dp[i][j-2]:
                        ''(None) can match with regular expressions like '.*' or 'a*'
                        so if dp[i][j-2] is True, and p[j-1] is '*', then no matter p[j-2] is '.' or letter, dp[i][j] is True,for example:
                            In a case, p[j-1] = '*', s[:i] = 'buaa', p[:j] = 'bua*b*'
                            To check if 'buaa' matches 'bua*b*':
                                'buaa' does not end with 'b'(the preceding element),
                                Check if 'buaa' matches 'bua*':
                                    If 'buaa' matches 'bua*',
                                    then we can say 'buaa' matches 'bua*b*'

                    Explanation for alternative2 dp[i][j] = (s[i-1] == p[j-2] or p[j-2] == '.' ) and dp[i-1][j]:
                        Reguar single step check, for example:
                            In a case, p[j-1] = '*', s[:i] = 'buaa', p[:j] = 'bua*'
                            To check if 'buaa' matches 'bua*':
                                'buaa' ends with 'a'(the preceding element),
                                Check if (('bua' matches 'bua*') and ('a' matches 'a'))
                    '''   
        return dp[m][n] # return the result of isMatch(s[:m], p[:n]), which is isMatch(s, p)

s = Solution()
print(s.isMatch("aab","c*a*b"))
            