class Solution:
    def countSubstrings(self, s: str) -> int:
        answer = []
        for i in s:
            answer.append(i)

        def expand(left, right):

            while left > 0 and right < len(s) - 1 and s[left] == s[right]:
                if s[left] == s[right]:
                    answer.append(s[left: right + 1])

                left -= 1
                right += 1


            if s[left] == s[right]:
                answer.append(s[left : right + 1])

        for i in range(1, len(s) - 1):
            expand(i - 1, i + 1)

        for i in range(1, len(s)):
            expand(i - 1, i)

        print(answer)
        print(len(answer))
        return len(answer)

s = Solution()
s.countSubstrings("hello")
