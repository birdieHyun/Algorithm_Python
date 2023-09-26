def solution(s, word_dict):

    dp = [0 for _ in range(len(s) + 1)]
    n = len(s)
    for i in range(4, n + 1):
        for word in word_dict:
            if s[i - len(word) : i] == word:
                dp[i] = max(dp[i - len(word) + 1] + 1, dp[i])

    return dp[n]


# 테스트
s1 = "centerminus"
word_dict1 = ["cent", "center", "term", "terminus", "rm", "min", "minus", "us"]
print(solution(s1, word_dict1))  # 기대값: 3

s2 = "aaaababab"
word_dict2 = ["aaa", "aaaa", "ab", "bab", "aababa"]
print(solution(s2, word_dict2))  # 기대값: 4

