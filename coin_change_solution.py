class Solution:
    def count_ways(self, coins, n, sum):
        dp = [sum + 1] * (sum + 1)
        dp[0] = 0
        
        for amount in range(1, sum + 1):
            for coin in coins:
                if coin <= amount:
                    dp[amount] = min(dp[amount], dp[amount - coin] + 1)
        
        minimum_coins = dp[sum] if dp[sum] != sum + 1 else -1
        return minimum_coins
