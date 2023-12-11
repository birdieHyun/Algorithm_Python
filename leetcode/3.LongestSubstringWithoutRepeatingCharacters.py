class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = ''
        answer = []
        for i in s:
            if i not in longest:
                longest += i
            else:
                dup_idx = longest.index(i)
                longest = longest[dup_idx + 1:]
                longest += i

            answer.append(len(longest))

        if not answer:
            return 0
        return max(answer)

s = Solution()
str = 'abcabcbb'
str = 'pwwkew'
str = ''

print(s.lengthOfLongestSubstring(str))



# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.