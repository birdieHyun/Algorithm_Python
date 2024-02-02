import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        missing = len(t)
        counter = collections.Counter(t)
        left = start = end = 0
        for right in range(1, len(t) + 1):
            missing -= counter(s[right - 1]) > 0
            counter[s[right]] -= 1
            if missing == 0:
                while left < right and counter[s[left]] < 0:
                    counter[s[left]] += 1
                    left += 1
                if not end or right - left <= end - start:
                    start, end = left, right
                    missing += 1
                    counter[s[left]] += 1
                    left += 1
        return s[start:end]