from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])
        for i in range(1, len(nums)):
            dp.append(max(dp[i - 1] + nums[i], nums[i]))

        return max(dp)


# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# nums length = 100_000
# O(n) 으로 풀어야 함 n log n
# 다음 값이 양수라면 max(이전 + 현재, 현재)
# 다음 값이
