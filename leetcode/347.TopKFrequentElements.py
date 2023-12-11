from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dicts = defaultdict(int)

        for i in nums:
            dicts[i] += 1

        nums_set = set(nums)

        answer_list = []

        for i in nums_set:
            answer_list.append((i, dicts[i]))

        answer_list.sort(reverse=True, key= lambda x : x[1])

        answer = []
        print(answer_list)
        for i in range(k):
            answer.append(answer_list[i][0])

        return answer

s = Solution()
nums = [1,1,1,2,2,3]
k = 2
# nums = [1]
# k = 1
# nums = [-1, -1]
# k = 1
# print(s.topKFrequent(nums, k))

# Output: [1,2]

# heapq 사용해서 풀어보기

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        q = []
        answer = []
        nums_set = set(nums)

        for i in nums_set:
            heapq.heappush(q, (-nums.count(i), i))

        for i in range(k):
            answer.append(heapq.heappop(q)[1])

        return answer

s = Solution()
nums = [1,1,1,1,2,2,3]
k = 2

# nums = [4,1,-1,2,-1,2,3]
# k = 2

print(s.topKFrequent(nums, k))
