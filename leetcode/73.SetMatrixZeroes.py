from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        zero_idx = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_idx.append((j, i))

        if zero_idx:
            for i in zero_idx:
                x, y = i
                matrix[y] = [0] * len(matrix[0])

                for j in range(len(matrix)):
                    matrix[j][x] = 0

        print(matrix)

# 리스트 순회하면서 첫 지점 찍고
# 찍은 지점 기준으로 상하좌우 다 0으로 변경
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s = Solution()

s.setZeroes(matrix)
