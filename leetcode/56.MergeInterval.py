from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge = []
        intervals.sort(key=lambda x : x[0])

        for start, end in intervals:

            if not merge:
                merge.append([start, end])
            elif merge[-1][1] < start:
                merge.append([start, end])
            else:
                merge[-1][1] = max(merge[-1][1], end)

        return merge



intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]

# intervals = [[1,4],[4,5]]
# Output: [[1,5]]

# intervals = [[1, 4], [2, 3]]
# Output : [[1, 4]]

intervals = [[1,4],[0,2],[3,5]]
# Output: [[0,5]]

s = Solution()
print(s.merge(intervals))