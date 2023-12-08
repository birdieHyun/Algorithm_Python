from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prefix_sum = [nums[0]]

        for i in range(1, len(nums)):
            prefix_sum.append(nums[i] + prefix_sum[i - 1])


        print(prefix_sum)
        return 0


nums = [-2,1,-3,4,-1,2,1,-5,4]
solution = Solution()
print(solution.maxSubArray(nums))

# -2  -1  -4  0  -1  1  2  -3  1
#  4  -1   0  2   1  5  2   3  1

# 인덱스 3부터 6까지가 최대

#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.


# Input: nums = [5, 4, -1, 7, 8]
# Output: 23
# Explanation: The subarray[5, 4, -1, 7, 8] has the largest sum 23.

# 1 <= nums.length <= 10^5  -> O(n log n) or O(n) 으로 해결
# -10^4 <= nums[i] <= 10^4