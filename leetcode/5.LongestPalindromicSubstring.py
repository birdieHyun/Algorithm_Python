class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1: right]

        answer = s[0]
        for i in range(1, len(s)):
            tmp = expand(i - 1, i + 1)
            if len(tmp) > len(answer):
                answer = tmp

        for i in range(1, len(s)):
            tmp = expand(i - 1, i)
            if len(tmp) > len(answer):
                answer = tmp

        return answer

s = Solution()
print(s.longestPalindrome("cbbd"))
