class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # Solution 1
        if coins == []:
            if amount == 0 :return 1
            else: return 0
        length = len(coins)
        dp = [[0 for i in range(amount + 1)] for j in range(len(coins))]
        for i in range(length):
            dp[i][0] = 1
        for i in range(length):
            for j in range(amount + 1):
                if j >= coins[i]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i]]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[length - 1][amount]
s = Solution()
print(s.change(201800,[1,5,10,25]))