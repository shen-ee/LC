class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Solution 1 144ms 130cases
        # length = len(s)
        # sum = 0
        # for i in range(0,length):
        #     j = 0
        #     while i-j>=0 and i+j<length:
        #         if s[i-j] == s[i+j]:
        #             sum += 1
        #             j += 1
        #         else:
        #             break
        #     j = 0
        #     while i-j>=0 and i+j+1<length:
        #         if s[i-j] == s[i+j+1]:
        #             sum += 1
        #             j += 1
        #         else:
        #             break
        # return sum

        # Solution 2 412ms
        l = len(s)
        dp = [[False for i in range (l+1)]for j in range (l+1)]
        sum = 0
        for i in range(0,l):
            for j in range(0,i+1):
                dp[j][i] = s[j] == s[i] and ( dp[j+1][i-1] or i-j < 3)
                if dp[j][i]:
                    sum += 1
                    # print(j,i)
        return sum


s = Solution()
str1 = "abcba"
print(s.countSubstrings(str1))