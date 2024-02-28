from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = 1
        zero_count = 0
        for i in nums:
            if i != 0:
                answer *= i
            else:
                zero_count += 1

        if zero_count >= 2:
            return [0] * len(nums)
        elif zero_count == 1:
            answers = []
            for i in nums:
                if i != 0:
                    answers.append(0)
                else:
                    answers.append(answer)
            return answers

        else:
            answers = []
            for i in nums:
                result = int(answer / i)
                answers.append(result)
            return answers


# 모두 다 곱함 (0이면 제외함)
# 0 이 몇개 있는지 확인하고
# 0이 한개라면 0 빼고 나머지 0 넣어줌
# 0이 두개 이상이라면 모두 0 처리
# 나머진 자기만큼만 나눠줌

s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))