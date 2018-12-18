class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # # Solution 1
        # dp = [False for i in range(len(s)+1)] # dp[i] means wordBreak(s[:i],wordDict)
        # dp[0] = True
        # for i in range(len(s)+1):
        #     for j in range(i)[::-1]:
        #         if dp[j] and s[j:i] in wordDict:
        #             dp[i] = True
        #             continue
        # return dp[-1]

        # Solution 1+
        wordDict = set(wordDict)
        maxlen = max([len(i) for i in wordDict]) if wordDict else 0
        dp = [False for i in range(len(s)+1)] # dp[i] means wordBreak(s[:i],wordDict)
        dp[0] = True
        for i in range(1,len(s)+1):
            dp[i] = any([(dp[j] and s[j:i] in wordDict) for j in range(i-maxlen, i)[::-1]])                  
        return dp[-1]

s = Solution()
str = "leetcode"
wordDict = ["leet", "code"]
re = s.wordBreak(str, wordDict)
print(re)