from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        for text in s:
            if text == '(' or text == '{' or text == '[':
                q.append(text)
            else:
                if not q:
                    return False
                tmp = q.pop()
                if tmp == '(':
                    if text != ')':
                        return False
                if tmp == '[':
                    if text != ']':
                        return False

                if tmp == '{':
                    if text != '}':
                        return False
        if q:
            return False

        return True

s = Solution()
print(s.isValid('()[]'))