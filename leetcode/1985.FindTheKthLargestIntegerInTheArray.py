from typing import List
import heapq


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        q = []
        for i in nums:
            heapq.heappush(q, -int(i))

        for i in range(k - 1):
            heapq.heappop(q)

        return str(-heapq.heappop(q))
