from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        answer = set()
        for i in nums:
            answer.add(i)

        return len(nums) != len(answer)