from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        buy = prices[0]
        for i in range(1, len(prices)):
            sell = prices[i]
            answer = max(answer, sell - buy)

            if buy > sell:
                buy = sell

        return answer
