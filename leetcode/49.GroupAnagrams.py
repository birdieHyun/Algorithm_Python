from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            anagram[key].append(s)
        answer = list(anagram.values())
        answer.sort(key=lambda x: len(x))
        return answer


s = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs))
