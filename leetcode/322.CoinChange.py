from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        if amount < coins[0]:
            return -1

        dp = [int(10e9)] * (amount + 1)

        for i in coins:
            if i < amount:
                dp[i] = 1

        for i in range(coins[0], amount + 1):
            if i in coins:
                continue
            else:
                for j in coins:
                    if j < amount and i > j:
                        a = dp[i]
                        b = dp[i - j] + 1
                        dp[i] = min(a, b)

        if dp[amount] != int(10e9):
            return dp[amount]

        return -1

# 예외 상황
# amount  < min(coins)
# amnount 만들 수 없을 경우 -1 반환


s = Solution()
# coins = [1, 2147483647]
# [102, 107, 186, 220, 336, 387, 418, 465]
coins = [102,220,186,465,336,107,387,418]
amount = 495
print(s.coinChange(coins, amount))