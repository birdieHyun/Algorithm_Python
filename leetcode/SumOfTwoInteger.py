class Solution:
    def getSum(self, a: int, b: int) -> int:

        answer = []
        tmp_a = a
        tmp_b = b
        if tmp_a < 0:
            tmp_a *= -1
        if tmp_b < 0:
            tmp_b *= -1

        for i in range(tmp_a):
            tmp = 1
            if a < 0:
                tmp = -1
            answer.append(tmp)

        for i in range(tmp_b):
            tmp = 1
            if b < 0:
                tmp = -1
            answer.append(tmp)

        return sum(answer)


solution = Solution()
a = 1
b = -1
print(solution.getSum(a, b))