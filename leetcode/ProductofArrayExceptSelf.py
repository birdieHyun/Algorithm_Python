from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        front = [1]
        end = [1]

        for i in range(len(nums) - 1):
            front.append(front[-1] * nums[i])

        for i in range(len(nums) - 1, 0, -1):
            end.insert(0, end[0] * nums[i])

        for i in range(len(nums)):
            answer.append(front[i] * end[i])

        return answer
