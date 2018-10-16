
def change(num):
    coins = [1,5,10,25]
    length = len(coins)
    num = 2018*100
    dp = [[0 for i in range(num+1)]for j in range(len(coins))]
    for i in range (length):
        dp[i][0] = 1
    for i in range(length):
        for j in range(num+1):
            if j >= coins[i]:
                dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
            else:
                dp[i][j] = dp[i-1][j]

    return dp[length-1][num]

print(change(2018))