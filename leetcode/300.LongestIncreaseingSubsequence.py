from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            maximum = 0

            for j in range(i):

                if nums[i] > nums[j] and dp[j] > maximum:
                    maximum = dp[j]

            dp[i] = maximum + 1

        return max(dp)

s = Solution()
nums = [10,9,2,5,3,7,101,18]
print(s.lengthOfLIS(nums))