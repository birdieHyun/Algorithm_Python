from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = []
        dp_minus = []
        dp.append(nums[0])
        dp_minus.append(nums[0])

        for i in range(1, len(nums)):
            dp.append(max(dp[i - 1] * nums[i], nums[i]))
            result = dp_minus[i - 1] * nums[i]
            if result < 0 and abs(result) > nums[i]:
                dp_minus.append(result)

            else:
                dp_minus.append(max(abs(dp_minus[i - 1] * nums[i]), nums[i]))

        print(dp)
        print(dp_minus)
        return max(max(dp), max(dp_minus))


s = Solution()
print(s.maxProduct([2,-5,-2,-4,3]))

# 마이너스 관리
