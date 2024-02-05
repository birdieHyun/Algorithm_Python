from typing import List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        q = []
        answer = []
        num_set = set(nums)

        for i in num_set:
            heapq.heappush(q, i)

        for i in range(len(nums)):
            answer.append(heapq.heappop(q))

            if len(answer) == k:
                return answer

        return answer
