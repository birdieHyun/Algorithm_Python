from collections import defaultdict
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        is_duplicated = defaultdict(int)

        for i in nums:
            if is_duplicated[i] >= 1:
                return True
            else:
                is_duplicated[i] += 1

        return False
