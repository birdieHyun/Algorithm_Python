from collections import deque


class Solution:
    def isPalindrome(self, s: str) -> bool:
        q = deque()

        for text in s:
            if text.isalnum():
                q.append(text.lower())

        for text in s:
            if text.isalnum():
                if text.lower() != q.pop():
                    return False

        return True


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
