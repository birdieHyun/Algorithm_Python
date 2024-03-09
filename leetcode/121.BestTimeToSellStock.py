from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        answer = 0
        for i in range(1, len(prices)):
            result = prices[i] - buy
            answer = max(result, answer)

            if result < 0:
                buy = prices[i]
        return answer

s = Solution()
print(s.maxProfit([7, 1, 5, 3, 6, 4]))

# 산 가격은 더 작아지면 무조건 새로 사는걸로 추정
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.