from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        dp = [False] * (len(nums) + 1)
        dp[1] = True

        for i in range(1, len(nums) + 1):
            now = nums[i - 1]
            if dp[i]:

                next = i + now + 1

                if next > len(nums):
                    next = len(nums) + 1

                for j in range(i, next):
                    dp[j] = True

        return dp[-1]

s = Solution()

nums = [2,3,1,1,4]
# nums = [3,2,1,0,4]

print(s.canJump(nums))