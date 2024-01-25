from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # interval 은 총 세 부분으로 나뉨
        # 왼쪽, 오른쪽, 병합된 가운데
        answer = []
        left, right = [], []

        for interval in intervals:
            if interval[1] < newInterval[0]:
                left.append(interval)
            elif interval[0] > newInterval[1]:
                right.append(interval)
            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])

        return left + [newInterval] + right


intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]

# intervals = [[1,3],[6,9]]
# newInterval = [2,5]

# intervals = []
# newInterval = [5, 7]

# intervals = [[1, 5]]
# newInterval = [2, 7]

# intervals = [[1, 5]]
# newInterval = [6, 8]

# intervals = [[1, 5]]
# newInterval = [0, 5]

# intervals = [[1, 5]]
# newInterval = [0, 0]

s = Solution()
print(s.insert(intervals, newInterval))
