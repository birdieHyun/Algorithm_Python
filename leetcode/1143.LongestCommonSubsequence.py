class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        len1 = len(text1) + 1
        len2 = len(text2) + 1

        dp = [[0] * len2 for _ in range(len1)]

        for i in range(1, len1):

            for j in range(1, len2):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]


text1 = "abcde"
text2 = "ace"

text1 = "ezupkr"
text2 = "ubmrapg"

text1 ="bsbininm"
text2 = "jmjkbkjkv"

s = Solution()
s.longestCommonSubsequence(text1, text2)
