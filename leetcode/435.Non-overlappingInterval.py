from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        answer = 0

        prev_end = intervals[0][1]

        for i in intervals[1:]:
            start, end = i[0], i[1]

            if start >= prev_end:
                prev_end = end
            else:
                answer += 1
                prev_end = min(end, prev_end)

        return answer


s = Solution()

# intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [[1, 100], [11, 22], [1, 11], [2, 12]]

print(s.eraseOverlapIntervals(intervals))
